using PropertyHook;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;

namespace EldenRingSurvivalMode.GameHook
{
    internal class ERHook : PHook
    {
        PHPointer FogInjectionAddr { get; set; }
        PHPointer FogNewmemPtr { get; set; }
        PHPointer EventFlags { get; set; }
        PHPointer StonePlatformEventFlags { get; set; }

        const string EventFlagsAOB = "48 8B 3D ? ? ? ? 48 85 FF 74 ? 48 8B 49";
        
        bool FogEnabled { get; set; }
        long BaseAddress { get; set; }

        const string windowName = "ELDEN RING™";
        const long fogInjAddress = 0x1B0C4B5;  // mov [rcx+0x00000120], rax
        const long freeAddress = 0x28C7800;
        static readonly byte[] originalMem = new byte[] { 0x48, 0x89, 0x81, 0x20, 0x01, 0x00, 0x00 };
        
        readonly List<(string name, int offset, int size)> gparamInjections = new List<(string, int, int)>()
        {
            ("NearDepth", 0x0C, 4),
            ("DrawTiming", 0x20, 4),
            ("FixedDensity", 0x40, 4),
            ("LocalLightScale", 0x48, 4),
            ("AbsorptionScale_Cyan", 0x70, 4),
            ("AbsorptionScale_Magenta", 0x74, 4),
            ("AbsorptionScale_Yellow", 0x78, 4),
            ("SkyColor_Red", 0x80, 4),
            ("SkyColor_Green", 0x84, 4),
            ("SkyColor_Blue", 0x88, 4),
            ("SkyColor_Alpha", 0x8C, 4),
            ("StartDist", 0x94, 4),
            ("DirectColor_Red", 0xC0, 4),
            ("DirectColor_Green", 0xC4, 4),
            ("DirectColor_Blue", 0xC8, 4),
            ("DirectColor_Alpha", 0xCC, 4),
        };

        int newmemValuesOffset = -1;

        public ERHook(int refreshInterval, int minLifetime) :
            base(refreshInterval, minLifetime, p => p.MainWindowTitle == windowName)
        {
            EventFlags = RegisterRelativeAOB(EventFlagsAOB, 3, 7, 0);
            StonePlatformEventFlags = new PHPointerChild(this, EventFlags, 0xC8);

            OnHooked += ERHook_OnHooked;
        }

        void ERHook_OnHooked(object sender, PHEventArgs e)
        {
            BaseAddress = Process.MainModule.BaseAddress.ToInt64();
            FogInjectionAddr = new PHPointerBase(this, (IntPtr)(BaseAddress + fogInjAddress));
            FogNewmemPtr = new PHPointerBase(this, (IntPtr)(BaseAddress + freeAddress));

            EnableEldenRingFog();
        }

        void ERHook_OnUnhooked(object sender, PHEventArgs e)
        {
            FogEnabled = false;
        }

        public bool Focused => Hooked && User32.GetForegroundProcessID() == Process.Id;

        public int GetIngameHour()
        {
            // Read hard-coded event flags to determine which hour the game is currently in, from 0 (midnight) to 23.
            // Returns -1 if no hour flag is active (e.g., game is not loaded) or an error occurs.
            
            long offset = StonePlatformEventFlags.Resolve().ToInt64();

            int hourFlagOffset = 0x1C204D + (1600 / 8);  // Hour0 = 19001600
            byte[] hourFlagBytes = StonePlatformEventFlags.ReadBytes(hourFlagOffset, 3);  // 24 flags
            string hourFlags = "";
            foreach (byte flag in hourFlagBytes)
            {
                hourFlags += Convert.ToString(flag, 2).PadLeft(8, '0');
            }
            if (hourFlags.Count(x => x == '1') > 1)
            {
                Console.WriteLine("ERROR: Time of day is ambiguous (multiple hour flags enabled).");
                return -1;
            }
            return hourFlags.IndexOf('1');
        }

        public void EnableEldenRingFog()
        {
            // Write assembly script and injection.
            if (FogEnabled)
                return;  // no need to enable again

#if DEBUG
            byte[] currentMem = Kernel32.ReadBytes(Handle, FogInjectionAddr.Resolve(), 7);
            Console.WriteLine($"Vanilla fog function bytes: {BitConverter.ToString(currentMem)}");
#endif

            IntPtr newmemPtr = FogNewmemPtr.Resolve();
            IntPtr injectionPtr = FogInjectionAddr.Resolve();
            long injectionAddr = injectionPtr.ToInt64();
            Console.WriteLine($"Injection address: {injectionAddr:X}");
            long newmemAddr = newmemPtr.ToInt64();
            Console.WriteLine($"Newmem address: {newmemAddr:X}");
            Console.WriteLine($"Expected newmem address: {FogNewmemPtr.Resolve().ToInt64():X}");

            // ORIGINAL CODE:
            // 48 89 81 20010000     mov [rcx+0x120], rax
            byte[] injectAsm = new byte[]
            {
                0xE9, 0x00, 0x00, 0x00, 0x00,  // jmp [newmem]
                0x90,  // nop
                0x90,  // nop
            };
            // Insert `jmp` offset into injection.
            int jmpNewmem = (int)(newmemAddr - (injectionAddr + 0x5));  // jumps AFTER jump instruction in game function (5 bytes)
            Array.Copy(BitConverter.GetBytes(jmpNewmem), 0, injectAsm, 0x1, 4);

            // New script that inserts values (and contains them at the end).
            // Built dynamically here based on all the values that need to be written.
            List<byte> newmemAsm = new List<byte>();

            // Original instruction: mov [rcx+0x120], rax
            newmemAsm.AddRange(originalMem);

            // push   r8
            newmemAsm.AddRange(new byte[] { 0x41, 0x50 });

            List<int> valueAddresses = new List<int>();
            foreach (var (name, offset, size) in gparamInjections)
            {
                // movabs r8 ...
                newmemAsm.AddRange(new byte[] { 0x49, 0xb8 });
                valueAddresses.Add(newmemAsm.Count);  // will write value offset here later
                // ... 0xFEFEFEFEFEFEFEFE (reserved)
                newmemAsm.AddRange(new byte[] { 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE, 0xFE });
                // xmm1,DWORD PTR [r8]
                newmemAsm.AddRange(new byte[] { 0xf3, 0x41, 0x0f, 0x10, 0x08 });
                // movss  DWORD PTR [rcx+{offset}],xmm1
                if (offset >= 0x80)
                {  // 32-bit offset required
                    byte[] offsetBytes = BitConverter.GetBytes(offset);
                    newmemAsm.AddRange(new byte[] { 0xf3, 0x0f, 0x11, 0x89, offsetBytes[0], offsetBytes[1], offsetBytes[2], offsetBytes[3] });
                }
                else
                {  // 8-bit offset can be used
                    newmemAsm.AddRange(new byte[] { 0xf3, 0x0f, 0x11, 0x49, (byte)offset });
                }
            }

            // pop    r8
            newmemAsm = newmemAsm.Concat(new byte[] { 0x41, 0x58 }).ToList();

            // jmp 
            int offsetAfterJmp = newmemAsm.Count + 5;
            int jmpReturn = (int)(injectionAddr + 0x7 - (newmemAddr + offsetAfterJmp));
            newmemAsm.Add(0xe9);
            newmemAsm.AddRange(BitConverter.GetBytes(jmpReturn));

            newmemValuesOffset = newmemAsm.Count;
            
            // Write values (placeholder zeroes) and insert 64-bit addresses (longs) into newmem.
            foreach (int offset in valueAddresses)
            {
                long absValueAddress = newmemAddr + newmemAsm.Count;
                byte[] addressBytes = BitConverter.GetBytes(absValueAddress);
                for (int i = 0; i < addressBytes.Length; i++)
                {
                    // Overwrite 0xFEFEFEFEFEFEFEFE placeholders in newmem.
                    newmemAsm[offset + i] = addressBytes[i];
                }
                // TODO: Use crafted default values from dictionary?
                newmemAsm.AddRange(new byte[] { 0x0, 0x0, 0x0, 0x0 });
            }

            byte[] newmemArray = newmemAsm.ToArray();
            Allocate(newmemPtr, (uint)newmemArray.Length, Kernel32.PAGE_EXECUTE_READWRITE);

#if DEBUG
            Console.WriteLine($"Fog script new memory allocated.");
#endif

            // `newmemAsm` is now complete.

            Console.WriteLine($"Final injection: {BitConverter.ToString(injectAsm)}");
            Console.WriteLine($"Final newmem: {BitConverter.ToString(newmemArray)}");
            
            //return;  // TODO

            if (!Kernel32.WriteBytes(Handle, newmemPtr, newmemArray))
            {
                // Script write failed. Do NOT inject, or it will crash the game.
                // Check if newmem script already seems to be there (based on first four bytes).
                Console.WriteLine($"Failed to write Elden Ring Fog assembly. Error: {Marshal.GetLastWin32Error()}");
                byte[] newmemExisting = Kernel32.ReadBytes(Handle, newmemPtr, 4);
                byte[] newmemAsmStart = new byte[4];
                Array.Copy(newmemArray, 0, newmemAsmStart, 0, 4);
                if (newmemExisting.SequenceEqual(newmemAsmStart))
                    Console.WriteLine("It appears the script has already been injected, so it may work anyway.");
                else
                    Console.WriteLine("The script does not appear to have already been injected.");
                return;
            }

            if (!Kernel32.WriteBytes(Handle, injectionPtr, injectAsm))
            {
                Console.WriteLine($"Failed to inject Elden Ring Fog assembly into game function. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("Fog effects will probably not work.");
            }
            else
            {
                Console.WriteLine("Enabled Elden Ring Fog script injection successfully.");
                FogEnabled = true;
            }
        }

        /// <summary>
        /// Update fog values in injected newmem script.
        /// 
        /// Values must already be converted to byte arrays from whatever their
        /// native type may be (usually `float`).
        /// </summary>
        /// <param name="values"></param>
        public void SetFogValues(params byte[][] values)
        {
            IntPtr fogNewmemPtr = FogNewmemPtr.Resolve();

            if (values.Length != gparamInjections.Count)
            {
                Console.WriteLine($"ERROR: Number of values passed to `SetFogValues` must match number of GPARAM values: {gparamInjections.Count}");
                return;
            }

            int valueOffset = newmemValuesOffset;
            for (int i = 0; i < values.Length; i++)
            {
                IntPtr valuePtr = IntPtr.Add(fogNewmemPtr, valueOffset);
                string name = gparamInjections[i].name;
                byte[] value = values[i];
                if (value.Length != gparamInjections[i].size)
                    throw new Exception($"INCORRECT FOG VALUE SIZE: {name}");
                bool writeSuccess = Kernel32.WriteBytes(Handle, valuePtr, value);
#if DEBUG
                if (!writeSuccess)
                    Console.WriteLine($"Attempted to set {name} to {BitConverter.ToString(value)}, but failed.");
                //else
                //    Console.WriteLine($"    --> {name} set to {BitConverter.ToString(value)}.");
#endif
                valueOffset += gparamInjections[i].size;
            }
        }

        public void DisableEldenRingFog()
        {
            // Free newmem and write original ASM back to fog function address.
            // Not actually used, but here for reference.

            Free(FogNewmemPtr.Resolve());
            Kernel32.WriteBytes(Handle, FogInjectionAddr.Resolve(), originalMem);
            FogEnabled = false;
        }
    }
}
