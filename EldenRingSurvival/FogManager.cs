using System.Diagnostics;
using System.Runtime.InteropServices;
using Erd_Tools;
using PropertyHook;

namespace EldenRingSurvival
{
    /// <summary>
    /// Memory injection and management for real-time modification
    /// of in-game lighting (to create more darkness, generally).
    /// 
    /// Currently only modifies 'Fog' GPARAM table.
    /// 
    /// TODO:
    ///     - Remove my old hacky event stuff and use Erd_Tools event flag methods.
    ///     - Locate the injection site properly, rather than hard-coding an address
    ///     that will keep changing as Elden Ring is updated.
    ///         (Looks like I already did this.)
    ///     - Use Erd_Tools method to write new memory? Otherwise I have to keep finding
    ///     free memory regions myself, which will also change as Elden Ring updates.
    /// </summary>
    internal class FogManager
    {
        public bool InjectionEnabled => LightingInjectionCodeAddr != null;

        ErdHook Hook { get; }
        nint Handle => Hook.Handle;
        Process Process => Hook.Process;

        PHPointer? LightingInjectionSiteAddr { get; set; } = null;  // found on hook with AOB
        IntPtr? LightingInjectionCodeAddr { get; set; } = null;  // allocated on enable with `GetPrefferedIntPtr()`
        long? BaseAddress { get; set; } = null;

        const long freeAddress = 0x294F600;  // 1.08

        // mov [rcx+0x00000120]
        const string FogInjectionAOB = "0F 10 82 10 01 00 00 0F 11 81 10 01 00 00 48 8B 82 20 01 00 00";
        
        // Instruction bytes replaced by jump instruction for injection. (Replicated immediately in new code.)
        // TODO: May need to replace the next instruction as well if an absolute/long jump offset is needed.
        static readonly byte[] replacedInstr = new byte[] { 0x48, 0x89, 0x81, 0x20, 0x01, 0x00, 0x00 };

        // Names, relative offsets, and sizes (currently all 4) of Fog GPARAM fields.
        List<(string name, int offset, uint size)> FogInjectionInfo { get; } = new()
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

        Dictionary<string, int> FogValueReadOffsets { get; set; } = new();
        Dictionary<string, int> FogValueWriteOffsets { get; set; } = new();

        public FogManager(ErdHook hook)
        {
            Hook = hook;
            
            LightingInjectionSiteAddr = Hook.RegisterAbsoluteAOB(FogInjectionAOB);
            Hook.OnHooked += Darkness_OnHooked;
            Hook.OnUnhooked += Darkness_OnUnhooked;
        }

        void Darkness_OnHooked(object? sender, PHEventArgs e)
        {
            BaseAddress = Process.MainModule?.BaseAddress.ToInt64();
            Console.WriteLine($"Elden Ring base address: {BaseAddress:X}");

            //EnableFogInjection();
        }

        void Darkness_OnUnhooked(object? sender, PHEventArgs e)
        {
            if (LightingInjectionCodeAddr != null)
            {
                // Free injection code memory.
                Hook.Free(LightingInjectionCodeAddr.Value);
                LightingInjectionCodeAddr = null;
            }
        }

        public (int hour, bool hasTorch, bool isOutdoors) GetIngameHourTorchOutdoors()
        {
            // Read hard-coded event flags to determine which hour the game is currently in, from 0 (midnight) to 23.
            // Returns -1 if no hour flag is active (e.g., game is not loaded) or an error occurs.

            bool playerHasTorch = Hook.IsEventFlag(19001584);
            Console.WriteLine($"Has Torch: {playerHasTorch}");

            // HACK: Currently checks flag 19001592 and returns 12 (noon) if enabled, so as to disable darkness.
            bool playerIsOutdoors = Hook.IsEventFlag(19001592);
            Console.WriteLine($"Is Outdoors: {playerIsOutdoors}");

            int currentHour = -1;
            int[] allHours = new int[24];
            for (int hour = 0; hour < 24; hour++)
            {
                if (Hook.IsEventFlag(19001600 + hour))
                {
                    allHours[hour] = 1;
                    if (currentHour == -1)
                    {
                        currentHour = hour;
                    }
                    else
                    {
                        Console.WriteLine($"ERROR: Time of day is ambiguous. Multiple hour flags enabled: at least {currentHour} and {hour}.");
                        return (-1, false, playerIsOutdoors);
                    }
                }
                else
                {
                    allHours[hour] = 0;
                }
            }

            string hoursString = "";
            foreach (int hour in allHours)
            {
                hoursString += hour.ToString();
            }
            Console.WriteLine($"HOUR FLAGS: {hoursString}");

            if (currentHour == -1)
                Console.WriteLine("ERROR: Could not detect time of day.");

            return (currentHour, playerHasTorch, playerIsOutdoors);
        }

        public void EnableFogInjection()
        {
            // Write assembly script and injection.
            if (InjectionEnabled)
                return;  // no need to enable again

            if (LightingInjectionSiteAddr == null)
            {
                Console.WriteLine("ERROR: Lighting memory injection site not found.");
                return;
            }
            if (BaseAddress == null)
            {
                Console.WriteLine("ERROR: Game base address not found.");
                return;
            }

            IntPtr siteAddr = LightingInjectionSiteAddr.Resolve() + 21;
            long siteAddrLong = siteAddr.ToInt64();
            Console.WriteLine($"Injection site address: {siteAddrLong:X}");

            // TODO: Need to construct injection code first, so we know how much space we need to allocate.
            MemBuilder lightingCode = GetInjectionCode();

            //IntPtr codeAddr = Hook.GetPrefferedIntPtr(lightingCode.Offset, siteAddr);  // ALLOCATED
            IntPtr codeAddr = (IntPtr)(BaseAddress.Value + freeAddress);
            Kernel32.VirtualAllocEx(Handle, IntPtr.Zero, lightingCode.Offset, Kernel32.MEM_COMMIT, Kernel32.PAGE_EXECUTE_READWRITE);

            if (codeAddr == IntPtr.Zero)
            {
                Console.WriteLine($"ERROR: Could not allocate memory of size {lightingCode.Offset} for lighting injection code.");
                return;
            }
            Console.WriteLine($"Lighting injection code address allocated: {codeAddr:X}");
            
            byte[] lightingCodeBytes = FillInjectionCodeOffsets(lightingCode, siteAddr, codeAddr);
            Console.WriteLine($"Final injection code: {BitConverter.ToString(lightingCodeBytes)}");

            //byte[] currentMem = Kernel32.ReadBytes(Handle, FogInjectionAddr.Resolve(), 7);
            //Console.WriteLine($"Vanilla fog function bytes: {BitConverter.ToString(currentMem)}");

            long codeAddrLong = codeAddr.ToInt64();

            // ORIGINAL CODE:
            // 48 89 81 20010000     mov [rcx+0x00000120], rax
            byte[] siteReplacementBytes = new byte[]
            {
                0xE9, 0x00, 0x00, 0x00, 0x00,  // jmp [newmem]
                0x90,  // nop
                0x90,  // nop
            };
            // Insert `jmp` offset into injection.
            int jmpCodeAddr = (int)(codeAddrLong - (siteAddrLong + 0x5));  // jumps AFTER jump instruction in game function (5 bytes)
            Array.Copy(BitConverter.GetBytes(jmpCodeAddr), 0, siteReplacementBytes, 0x1, 4);

            if (!Kernel32.WriteBytes(Handle, codeAddr, lightingCodeBytes))
            {
                // Script write failed. Do NOT inject, or it will crash the game.
                // Check if code script already seems to be there (based on first four bytes).
                Console.WriteLine($"Failed to write Elden Ring Fog assembly. Error: {Marshal.GetLastWin32Error()}");
                byte[] codeExisting = Kernel32.ReadBytes(Handle, codeAddr, 4);
                byte[] codeAsmStart = new byte[4];
                Array.Copy(lightingCodeBytes, 0, codeAsmStart, 0, 4);
                if (codeExisting.SequenceEqual(codeAsmStart))
                    Console.WriteLine("It appears the script has already been injected, so it may work anyway.");
                else
                    Console.WriteLine("The script does NOT appear to have already been injected.");

                return;
            }

            // Code was written successfully, so we now try to write the code jump instruction to the injection site.
            if (!Kernel32.WriteBytes(Handle, siteAddr, siteReplacementBytes))
            {
                Console.WriteLine($"Failed to inject Elden Ring Fog assembly into game function. Error: {Marshal.GetLastWin32Error()}");
                Console.WriteLine("Fog effects will probably not work.");
                Hook.Free(codeAddr);  // free injected code
            }
            else
            {
                //Console.WriteLine("Enabled Elden Ring Fog script injection successfully.");
                LightingInjectionCodeAddr = codeAddr;  // stored for freeing later
            }
        }

        /// <summary>
        /// New code that inserts values (and contains them at the end).
        /// Also moves actual GPARAM values from rcx to static memory so they can be read.
        /// Built dynamically here based on all the values that need to be written.
        /// 
        /// Returned `MemBuilder` instance just needs its relative jump offset written,
        /// which can be done after a region of required size has been allocated for this 
        /// code.
        /// </summary>
        /// <returns></returns>
        MemBuilder GetInjectionCode()
        {            
            MemBuilder lightingCode = new();

            // Original instruction: mov [rcx+0x00000120], rax
            lightingCode.Write(replacedInstr);

            //// TODO: Debugging with a very simple test script.
            //// jmp 
            //lightingCode.Write("e9");
            //lightingCode.Reserve("JUMP_BACK", 4);
            //return lightingCode;

            // push r8
            lightingCode.Write("41 50");

            foreach (var (name, offset, size) in FogInjectionInfo)
            {
                // READ ORIGINAL VALUE from `rdx`

                // movabs r8, [newmemReadOffset]
                lightingCode.Write("49 b8");
                lightingCode.Reserve(name + "_READ", 8);

                // movss xmm1, DWORD PTR [rdx+{offset}]
                if (offset >= 0x80)
                {  // 32-bit offset required
                    lightingCode.Write("f3 0f 10 8a");
                    byte[] offsetBytes = BitConverter.GetBytes(offset);
                    lightingCode.Write(offsetBytes);
                }
                else
                {  // 8-bit offset can be used
                    lightingCode.Write("f3 0f 10 4a");
                    lightingCode.Write((byte)offset);
                }
                // movss DWORD PTR [r8], xmm1
                lightingCode.Write("f3 41 0f 11 08");
                // Original value now written at the end of `newmem` (`newmemReadOffset`).

                // WRITE NEW VALUE to `rcx`

                // movabs r8, [newmemWriteOffset]
                lightingCode.Write("49 b8");
                lightingCode.Reserve(name + "_WRITE", 8);

                // movss xmm1, DWORD PTR [r8]
                lightingCode.Write("f3 41 0f 10 08");

                // movss DWORD PTR [rcx+{offset}], xmm1
                if (offset >= 0x80)
                {  // 32-bit offset required
                    lightingCode.Write("f3 0f 11 89");
                    byte[] offsetBytes = BitConverter.GetBytes(offset);
                    lightingCode.Write(offsetBytes);
                }
                else
                {  // 8-bit offset can be used
                    lightingCode.Write("f3 0f 11 49");
                    lightingCode.Write((byte)offset);
                }
                // New value now written to `[rcx+{offset}]`.
            }

            // pop r8
            lightingCode.Write("41 58");

            // jmp 
            lightingCode.Write("e9");
            lightingCode.Reserve("JUMP_BACK", 4);

            // Write placeholder zeroes for read/write GPARAM values.
            // We need this code to be allocated before we can fill the
            // absolute addresses of these integers in the script above.
            for (int i = 0; i < 2 * FogInjectionInfo.Count; i++)
                lightingCode.Write("00 00 00 00");
            // TODO: Use crafted default values from dictionary for initial write values?

            return lightingCode;
        }

        /// <summary>
        /// Finish writing new injection code once it has been allocated to `codeOffset`.
        /// </summary>
        /// <param name="lightingCode"></param>
        /// <param name="siteAddr"></param>
        /// <param name="codeAddr"></param>
        byte[] FillInjectionCodeOffsets(MemBuilder lightingCode, nint siteAddr, nint codeAddr)
        {
            // jmp
            int jumpOffset = lightingCode.GetReservedOffset("JUMP_BACK");
            int offsetAfterJmp = jumpOffset + 5;
            // TODO: I seem to be landing 1 byte too early. Testing a simple +1.
            int jmpReturn = (int)(siteAddr + 0x7 - (codeAddr + offsetAfterJmp)) + 1;
            lightingCode.Fill("JUMP_BACK", BitConverter.GetBytes(jmpReturn));

            //// TODO: Simple test.
            //return lightingCode.Finish();

            // Initial value offset.
            int valueOffset = jumpOffset + 4;

            foreach (var (name, offset, size) in FogInjectionInfo)
            {
                long absAddress = (codeAddr + valueOffset).ToInt64();
                byte[] absAddressBytes = BitConverter.GetBytes(absAddress);
                lightingCode.Fill(name + "_READ", absAddressBytes);
                FogValueReadOffsets[name] = valueOffset;
                valueOffset += 4;
            }

            // Write values (placeholder zeroes) and insert 64-bit addresses (longs) into newmem.
            foreach (var (name, offset, size) in FogInjectionInfo)
            {
                long absAddress = (codeAddr + valueOffset).ToInt64();
                byte[] absAddressBytes = BitConverter.GetBytes(absAddress);
                lightingCode.Fill(name + "_WRITE", absAddressBytes);
                FogValueWriteOffsets[name] = valueOffset;                
                valueOffset += 4;
            }

            return lightingCode.Finish();
        }

        public Dictionary<string, byte[]?>? GetOriginalFogValues()
        {
            if (LightingInjectionCodeAddr == null)
            {
                Console.WriteLine("ERROR: Could not get current injected lighting values. Lighting code not injected.");
                return null;
            }

            Dictionary<string, byte[]?> values = new();

            foreach (var (name, _, size) in FogInjectionInfo)
            {
                if (!FogValueReadOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Cannot read lighting field: '{name}'. Read offset not set.");
                    values[name] = null;
                    continue;
                }
                int valueOffset = FogValueReadOffsets[name];
                IntPtr valuePtr = IntPtr.Add(LightingInjectionCodeAddr.Value, valueOffset);
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
        public bool SetInjectedFogValues(Dictionary<string, byte[]> values)
        {
            if (LightingInjectionCodeAddr == null)
            {
                Console.WriteLine("ERROR: Could not set injected fog values. Lighting code not injected.");
                return false;
            }

            foreach (string name in values.Keys)
            {
                if (!FogValueWriteOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Invalid fog value name: '{name}'. No data written.");
                    return false;
                }
            }

            foreach (var (name, _, size) in FogInjectionInfo)
            {
                if (!values.ContainsKey(name))
                    continue;

                if (!FogValueWriteOffsets.ContainsKey(name))
                {
                    Console.WriteLine($"ERROR: Cannot write fog value: '{name}'. Write offset not set.");
                    continue;
                }
                int valueOffset = FogValueWriteOffsets[name];
                IntPtr valuePtr = IntPtr.Add(LightingInjectionCodeAddr.Value, valueOffset);
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

        public void DisableFogInjection()
        {
            // Free newmem and write original ASM back to fog function address.
            // Not actually used, but here for reference.

            if (LightingInjectionCodeAddr == null)
            {
                return;  // nothing to disable
            }

            Hook.Free(LightingInjectionCodeAddr.Value);
            LightingInjectionCodeAddr = null;
            if (LightingInjectionSiteAddr != null)
                Kernel32.WriteBytes(Handle, LightingInjectionSiteAddr.Resolve() + 21, replacedInstr);            
        }
    }
}
