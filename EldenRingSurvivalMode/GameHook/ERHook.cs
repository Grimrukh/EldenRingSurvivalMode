using PropertyHook;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;

namespace EldenRingSurvivalMode.GameHook
{
    internal class ERHook : PHook
    {
        class MemBuilder
        {
            readonly List<byte> mem = new List<byte>();
            readonly Dictionary<string, (int, int)> reserved = new Dictionary<string, (int, int)>();

            public int Offset => mem.Count;

            List<byte> ParseHexString(string hex)
            {
                List<byte> result = new List<byte>();
                foreach (string b in hex.Split(' '))
                    result.Add(byte.Parse(b, System.Globalization.NumberStyles.AllowHexSpecifier));
                return result;
            }

            public void Write(IEnumerable<byte> bytes)
            {
                mem.AddRange(bytes);
            }

            public void Write(string hex)
            {
                Write(ParseHexString(hex));
            }
            
            public void Write(byte b)
            {
                mem.Add(b);
            }

            public byte[] Finish()
            {
                if (reserved.Count > 0)
                    throw new Exception("Cannot call `MemBuilder.Finish()` when reserved names remain.");
                return mem.ToArray();
            }

            public void Reserve(string name, int size)
            {
                if (reserved.ContainsKey(name))
                    throw new Exception($"Name '{name}' is already reserved.");
                reserved[name] = (size, Offset);
                for (int i = 0; i < size; i++)
                    Write(0xFE);  // placeholder bytes
            }

            public void Fill(string name, IEnumerable<byte> value)
            {
                if (!reserved.ContainsKey(name))
                    throw new Exception($"Cannot fill unreserved name '{name}'");
                (int size, int offset) = reserved[name];
                byte[] valueArray = value.ToArray();
                if (valueArray.Length != size)
                    throw new Exception($"Number of bytes to write to reserved '{name}' does not match reserved size: {size}");
                for (int i = 0; i < valueArray.Length; i++)
                    mem[offset + i] = valueArray[i];
                reserved.Remove(name);
            }

            public void Fill(string name, string hex)
            {
                Fill(name, ParseHexString(hex));
            }
        }

        PHPointer FogInjectionAddr { get; set; }
        PHPointer FogNewmemPtr { get; set; }
        PHPointer EventFlags { get; set; }
        PHPointer StonePlatformEventFlags { get; set; }
        const int StonePlatformEventOffset = 0x1C204D;  // offset of event flag 19000000

        const string EventFlagsAOB = "48 8B 3D ? ? ? ? 48 85 FF 74 ? 48 8B 49";
        
        bool FogEnabled { get; set; }
        long BaseAddress { get; set; }

        const string windowName = "ELDEN RING™";
        const long fogInjAddress = 0x1B0C4B5;  // mov [rcx+0x00000120], rax
        const long freeAddress = 0x28C7800;
        static readonly byte[] originalMem = new byte[] { 0x48, 0x89, 0x81, 0x20, 0x01, 0x00, 0x00 };
        
        readonly List<(string name, int offset, uint size)> gparamInjections = new List<(string, int, uint)>()
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

        Dictionary<string, int> FogValueReadOffsets { get; set; } = new Dictionary<string, int>();
        Dictionary<string, int> FogValueWriteOffsets { get; set; } = new Dictionary<string, int>();

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

            // HACK: Currently checks flag 1592 and returns 12 (noon) if enabled, so as to disable darkness.
            //byte playerIsOutdoors = StonePlatformEventFlags.ReadByte(StonePlatformEventOffset + (1592 / 8));
            //Console.WriteLine($"Outdoors: {playerIsOutdoors}");
            //if (playerIsOutdoors == 0)
            //    return 12;  // MIDDAY

            int hourFlagOffset = StonePlatformEventOffset + (1600 / 8);  // Hour0 = 19001600
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

            //byte[] currentMem = Kernel32.ReadBytes(Handle, FogInjectionAddr.Resolve(), 7);
            //Console.WriteLine($"Vanilla fog function bytes: {BitConverter.ToString(currentMem)}");

            IntPtr newmemPtr = FogNewmemPtr.Resolve();
            IntPtr injectionPtr = FogInjectionAddr.Resolve();
            long injectionAddr = injectionPtr.ToInt64();
            //Console.WriteLine($"Injection address: {injectionAddr:X}");
            long newmemAddr = newmemPtr.ToInt64();
            //Console.WriteLine($"Newmem address: {newmemAddr:X}");
            //Console.WriteLine($"Expected newmem address: {FogNewmemPtr.Resolve().ToInt64():X}");

            // ORIGINAL CODE:
            // 48 89 81 20010000     mov [rcx+0x00000120], rax
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
            // Also moves actual GPARAM values from rcx to static memory so they can be read.
            // Built dynamically here based on all the values that need to be written.
            MemBuilder newmem = new MemBuilder();

            // Original instruction: mov [rcx+0x00000120], rax
            newmem.Write(originalMem);

            // push r8
            newmem.Write("41 50");

            foreach (var (name, offset, size) in gparamInjections)
            {
                // READ ORIGINAL VALUE from `rdx`

                // movabs r8, [newmemReadOffset]
                newmem.Write("49 b8");
                newmem.Reserve(name + "_READ", 8);

                // movss xmm1, DWORD PTR [rdx+{offset}]
                if (offset >= 0x80)
                {  // 32-bit offset required
                    newmem.Write("f3 0f 10 8a");
                    byte[] offsetBytes = BitConverter.GetBytes(offset);
                    newmem.Write(offsetBytes);
                }
                else
                {  // 8-bit offset can be used
                    newmem.Write("f3 0f 10 4a");
                    newmem.Write((byte)offset);
                }
                // movss DWORD PTR [r8], xmm1
                newmem.Write("f3 41 0f 11 08");

                // WRITE NEW VALUE to `rcx`

                // movabs r8 [newmemWriteOffset]
                newmem.Write("49 b8");
                newmem.Reserve(name + "_WRITE", 8);
                
                // xmm1,DWORD PTR [r8]
                newmem.Write("f3 41 0f 10 08");
                
                // movss  DWORD PTR [rcx+{offset}],xmm1
                if (offset >= 0x80)
                {  // 32-bit offset required
                    newmem.Write("f3 0f 11 89");
                    byte[] offsetBytes = BitConverter.GetBytes(offset);
                    newmem.Write(offsetBytes);
                }
                else
                {  // 8-bit offset can be used
                    newmem.Write("f3 0f 11 49");
                    newmem.Write((byte)offset);
                }
            }

            // pop r8
            newmem.Write("41 58");

            // jmp 
            int offsetAfterJmp = newmem.Offset + 5;
            int jmpReturn = (int)(injectionAddr + 0x7 - (newmemAddr + offsetAfterJmp));
            newmem.Write("e9");
            newmem.Write(BitConverter.GetBytes(jmpReturn));

            foreach (var (name, offset, size) in gparamInjections)
            {
                long absValueAddress = newmemAddr + newmem.Offset;
                byte[] addressBytes = BitConverter.GetBytes(absValueAddress);
                newmem.Fill(name + "_READ", addressBytes);
                FogValueReadOffsets[name] = newmem.Offset;
                newmem.Write("00 00 00 00");
            }

            // Write values (placeholder zeroes) and insert 64-bit addresses (longs) into newmem.
            foreach (var (name, offset, size) in gparamInjections)
            {
                long absValueAddress = newmemAddr + newmem.Offset;
                byte[] addressBytes = BitConverter.GetBytes(absValueAddress);
                newmem.Fill(name + "_WRITE", addressBytes);
                FogValueWriteOffsets[name] = newmem.Offset;
                // TODO: Use crafted default values from dictionary?
                newmem.Write("00 00 00 00");
            }

            byte[] newmemArray = newmem.Finish();
            Allocate(newmemPtr, (uint)newmemArray.Length, Kernel32.PAGE_EXECUTE_READWRITE);

#if DEBUG
            //Console.WriteLine($"Fog script new memory allocated.");
#endif

            //Console.WriteLine($"Final injection: {BitConverter.ToString(injectAsm)}");
            //Console.WriteLine($"Final newmem: {BitConverter.ToString(newmemArray)}");
            
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
                //Console.WriteLine("Enabled Elden Ring Fog script injection successfully.");
                FogEnabled = true;
            }
        }

        public Dictionary<string, byte[]> GetFogValues()
        {
            IntPtr fogNewmemPtr = FogNewmemPtr.Resolve();

            Dictionary<string, byte[]> values = new Dictionary<string, byte[]>();

            foreach (var (name, _, size) in gparamInjections)
            {
                if (!FogValueReadOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Cannot read fog value: '{name}'. Read offset not set.");
                    values[name] = null;
                    continue;
                }                
                int valueOffset = FogValueReadOffsets[name];
                IntPtr valuePtr = IntPtr.Add(fogNewmemPtr, valueOffset);
                byte[] value = Kernel32.ReadBytes(Handle, valuePtr, size);
                values[name] = value;
            }

            return values;
        }

        /// <summary>
        /// Update fog values in injected newmem script.
        /// 
        /// Values must already be converted to byte arrays from whatever their
        /// native type may be (usually `float`).
        /// </summary>
        /// <param name="values"></param>
        public bool SetFogValues(Dictionary<string, byte[]> values)
        {
            foreach (string name in values.Keys)
            {
                if (!FogValueWriteOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Invalid fog value name: '{name}'. No data written.");
                    return false;
                }
            }

            IntPtr fogNewmemPtr = FogNewmemPtr.Resolve();

            foreach (var (name, _, size) in gparamInjections)
            {
                if (!values.ContainsKey(name))
                    continue;

                if (!FogValueWriteOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Cannot write fog value: '{name}'. Write offset not set.");
                    values[name] = null;
                    continue;
                }
                int valueOffset = FogValueWriteOffsets[name];
                IntPtr valuePtr = IntPtr.Add(fogNewmemPtr, valueOffset);
                byte[] value = values[name];
                if (value.Length != size)
                    throw new Exception($"INCORRECT FOG VALUE SIZE: {name}");
                bool writeSuccess = Kernel32.WriteBytes(Handle, valuePtr, value);
#if DEBUG
                if (!writeSuccess)
                    Console.WriteLine($"Attempted to set {name} to {BitConverter.ToString(value)}, but failed.");
                //else
                //    Console.WriteLine($"    --> {name} set to {BitConverter.ToString(value)}.");
#endif
            }

            return true;
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
