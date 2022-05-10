using PropertyHook;
using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;

namespace EldenRingSurvivalMode.GameHook
{
    internal class ERHook : PHook
    {
        PHPointer FogInjectionAddr { get; set; }
        PHPointer FogNewmemPtr { get; set; }
        PHPointer EventFlags { get; set; }

        bool FogEnabled { get; set; }

        const string windowName = "ELDEN RING™";
        const long baseAddress = 0x7FF7E0D20000;
        const long fogInjAddress = 0x1B0C3CD + 7;  // after instruction that reads rdx into xmm1
        const long freeAddress = 0x28C7800;
        const int newmemJumpOffset = 0x4B;  // offset to write jump size in newmem
        readonly int[] newmemValueOffsets = new int[] { 0x4F, 0x53, 0x57 };  // offsets of fog values at end of newmem
        
        public ERHook(int refreshInterval, int minLifetime) :
            base(refreshInterval, minLifetime, p => p.MainWindowTitle == windowName)
        {
            FogInjectionAddr = new PHPointerBase(this, (IntPtr)(baseAddress + fogInjAddress));
            FogNewmemPtr = new PHPointerBase(this, (IntPtr)(baseAddress + freeAddress));
            
            // TODO: Check ER cheat table for AOB and offsets.
            EventFlags = RegisterRelativeAOB(DSROffsets.EventFlagsAOB, 3, 7, DSROffsets.EventFlagsOffset1, DSROffsets.EventFlagsOffset2);

            OnHooked += DSRHook_OnHooked;
        }

        void DSRHook_OnHooked(object sender, PHEventArgs e)
        {
            EnableEldenRingFog();
        }

        public bool Focused => Hooked && User32.GetForegroundProcessID() == Process.Id;

        void EnableEldenRingFog()
        {
            // Write assembly script and injection.

#if DEBUG
            byte[] currentMem = Kernel32.ReadBytes(Handle, FogInjectionAddr.Resolve(), 7);
            Console.WriteLine($"Vanilla fog function bytes: {BitConverter.ToString(currentMem)}");
#endif

            // ORIGINAL CODE:
            // 0f 29 89 90 00 00 00     movaps XMMWORD PTR [rcx+0x90],xmm1
            byte[] injectAsm = new byte[]
            {
                0xE9, 0x00, 0x00, 0x00, 0x00,  // jmp [newmem]
                0x90,  // nop
                0x90,  // nop
            };

            // New script that inserts values (and contains them at the end).
            byte[] newmemAsm = ERAssembly.EldenRingFog;
            //byte[] newmemAsm = new byte[] { 0xE9, 0x00, 0x00, 0x00, 0x00 };

            // Note that this address-specific override of `Allocate()` uses `MEM_RESERVE | MEM_COMMIT`, not just `MEM_COMMIT`.
            IntPtr newmemPtr = FogNewmemPtr.Resolve();
            // TODO: Check if this succeeds. I think it may not, but I already have write access.
            Allocate(newmemPtr, (uint)newmemAsm.Length, Kernel32.PAGE_EXECUTE_READWRITE);
            IntPtr injectionPtr = FogInjectionAddr.Resolve();

#if DEBUG
            Console.WriteLine($"Fog script new memory allocated.");
#endif

            long injectionAddr = injectionPtr.ToInt64();
            Console.WriteLine($"Injection address: {injectionAddr:X}");
            long newmemAddr = newmemPtr.ToInt64();
            Console.WriteLine($"Newmem address: {newmemAddr:X}");
            Console.WriteLine($"Expected newmem address: {FogNewmemPtr.Resolve().ToInt64():X}");

            // Put allocated 64-bit addresses into new script (from the end of the same script).
            Array.Copy(BitConverter.GetBytes(newmemAddr + newmemValueOffsets[0]), 0, newmemAsm, 0x0B, 8);  // Fog start multiplier
            Array.Copy(BitConverter.GetBytes(newmemAddr + newmemValueOffsets[1]), 0, newmemAsm, 0x1F, 8);  // Density near
            Array.Copy(BitConverter.GetBytes(newmemAddr + newmemValueOffsets[2]), 0, newmemAsm, 0x33, 8);  // Alpha

            // Calculate and insert `jmp` offsets (always the same, in practice).
            int jmpNewmem = (int)(newmemAddr - (injectionAddr + 0x5));  // jumps AFTER jump instruction in game function (5 bytes)
            Array.Copy(BitConverter.GetBytes(jmpNewmem), 0, injectAsm, 0x1, 4);
            int jmpReturn = (int)(injectionAddr + 0x7 - (newmemAddr + newmemValueOffsets[0]));  // jumps AFTER jump instruction in newmem
            Array.Copy(BitConverter.GetBytes(jmpReturn), 0, newmemAsm, newmemJumpOffset, 4);
            
            // TODO: Debugging injection
            //int jmpReturn = (int)(injectionAddr + 0x7 - (newmemAddr + 0x5));  // jumps AFTER jump instruction in newmem
            //Array.Copy(BitConverter.GetBytes(jmpReturn), 0, newmemAsm, 0x1, 4);

            Console.WriteLine($"Final newmem: {BitConverter.ToString(newmemAsm)}");
            Console.WriteLine($"Final injection: {BitConverter.ToString(injectAsm)}");

            if (!Kernel32.WriteBytes(Handle, newmemPtr, newmemAsm))
            {
                // Script write failed. Do NOT inject, or it will crash the game.
                Console.WriteLine($"Failed to write Elden Ring Fog assembly. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("(This may be because the script was already injected, in which case it should work anyway.)");
                return;
            }

            if (!Kernel32.WriteBytes(Handle, injectionPtr, injectAsm))
            {
                Console.WriteLine($"Failed to inject Elden Ring Fog assembly into game function. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("Fog effects will probably not work.");
            }
            else
            {
                Console.WriteLine($"Enabled Elden Ring Fog script injection successfully.");
                FogEnabled = true;
            }
        }

        public void SetFogValues(float startMultiplier, float densityNear, float alpha)
        {
            IntPtr fogNewmemPtr = FogNewmemPtr.Resolve();

            IntPtr startMultiplierPtr = IntPtr.Add(fogNewmemPtr, newmemValueOffsets[0]);
            IntPtr densityNearPtr = IntPtr.Add(fogNewmemPtr, newmemValueOffsets[1]);
            IntPtr alphaPtr = IntPtr.Add(fogNewmemPtr, newmemValueOffsets[2]);

            bool startMultiplierSuccess = Kernel32.WriteBytes(Handle, startMultiplierPtr, BitConverter.GetBytes(startMultiplier));
            bool densityNearSuccess = Kernel32.WriteBytes(Handle, densityNearPtr, BitConverter.GetBytes(densityNear));
            bool alphaSuccess = Kernel32.WriteBytes(Handle, alphaPtr, BitConverter.GetBytes(alpha));

#if DEBUG
            //if (!startMultiplierSuccess)
            //    Console.WriteLine($"Attempt to set FOG START MULTIPLIER to {startMultiplier}, but failed.");
            //else
            //    Console.WriteLine($"--> FOG START MULTIPLIER set to {startMultiplier}.");
            //if (!densityNearSuccess)
            //    Console.WriteLine($"Attempt to set FOG NEAR DENSITY to {densityNear}, but failed.");
            //else
            //    Console.WriteLine($"--> FOG NEAR DENSITY set to {densityNear}.");
            //if (!alphaSuccess)
            //    Console.WriteLine($"Attempt to set FOG ALPHA to {alpha}, but failed.");
            //else
            //    Console.WriteLine($"--> FOG ALPHA set to {alpha}.");
#endif
        }

        public void DisableEldenRingFog()
        {
            // Free newmem and write original ASM back to fog function address.
            // Not actually used, but here for reference.

            Free(FogNewmemPtr.Resolve());
            byte[] defaultAsm = new byte[] { 0x0f, 0x29, 0x89, 0x90, 0x00, 0x00, 0x00 };
            Kernel32.WriteBytes(Handle, FogInjectionAddr.Resolve(), defaultAsm);
            FogEnabled = false;
        }

        #region Flags
        static Dictionary<string, int> EventFlagGroups { get; } = new Dictionary<string, int>()
        {
            {"0", 0x00000},
            {"1", 0x00500},
            {"5", 0x05F00},
            {"6", 0x0B900},
            {"7", 0x11300},
        };

        static Dictionary<string, int> EventFlagAreas { get; } = new Dictionary<string, int>()
        {
            {"000", 00},
            {"100", 01},
            {"101", 02},
            {"102", 03},
            {"110", 04},
            {"120", 05},
            {"121", 06},
            {"130", 07},
            {"131", 08},
            {"132", 09},
            {"140", 10},
            {"141", 11},
            {"150", 12},
            {"151", 13},
            {"160", 14},
            {"170", 15},
            {"180", 16},
            {"181", 17},
        };

        int GetEventFlagOffset(int ID, out uint mask)
        {
            string idString = ID.ToString("D8");
            if (idString.Length == 8)
            {
                string group = idString.Substring(0, 1);
                string area = idString.Substring(1, 3);
                int section = Int32.Parse(idString.Substring(4, 1));
                int number = Int32.Parse(idString.Substring(5, 3));

                if (EventFlagGroups.ContainsKey(group) && EventFlagAreas.ContainsKey(area))
                {
                    int offset = EventFlagGroups[group];
                    offset += EventFlagAreas[area] * 0x500;
                    offset += section * 128;
                    offset += (number - (number % 32)) / 8;

                    mask = 0x80000000 >> (number % 32);
                    return offset;
                }
            }
            throw new ArgumentException("Unknown event flag ID: " + ID);
        }

        public bool ReadEventFlag(int ID)
        {
            int offset = GetEventFlagOffset(ID, out uint mask);
            return EventFlags.ReadFlag32(offset, mask);
        }

        public void WriteEventFlag(int ID, bool state)
        {
            int offset = GetEventFlagOffset(ID, out uint mask);
            EventFlags.WriteFlag32(offset, mask, state);
        }

        public void EnableEventFlag(int ID)
        {
            WriteEventFlag(ID, true);
        }

        public void DisableEventFlag(int ID)
        {
            WriteEventFlag(ID, false);
        }
        #endregion
    }
}
