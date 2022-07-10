using SoulsFormats;
using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;
using System.Threading;
using EldenRingSurvivalMode.GameHook;

namespace EldenRingSurvivalMode
{
    internal class Program
    {
        enum DarknessLevel
        {
            None = -1,
            Low = 0,
            Medium = 1,
            High = 2,
        }

        static int DarknessDrawTiming = 2;  // Show VFX

        static readonly Dictionary<DarknessLevel, Dictionary<string, float>> DarknessPresets = new Dictionary<DarknessLevel, Dictionary<string, float>>()
        {
            [DarknessLevel.Low] = new Dictionary<string, float>()
            {
                ["NearDepth"] = 10f,
                //["DrawTiming"] = 2,
                ["FixedDensity"] = 0.05f,
                ["LocalLightScale"] = 0.02f,
                ["AbsorptionScale_Cyan"] = 0.5f,
                ["AbsorptionScale_Magenta"] = 0.5f,
                ["AbsorptionScale_Yellow"] = 0.5f,
                ["SkyColor_Red"] = 0f,
                ["SkyColor_Green"] = 0f,
                ["SkyColor_Blue"] = 0f,
                ["SkyColor_Alpha"] = 0f,
                ["StartDist"] = 150f,
                ["DirectColor_Red"] = 0.4f,
                ["DirectColor_Green"] = 0.4f,
                ["DirectColor_Blue"] = 0.4f,
                ["DirectColor_Alpha"] = 0.4f,
            },
            [DarknessLevel.Medium] = new Dictionary<string, float>()
            {
                ["NearDepth"] = 8f,
                //["DrawTiming"] = 2,
                ["FixedDensity"] = 0.15f,
                ["LocalLightScale"] = 0.02f,
                ["AbsorptionScale_Cyan"] = 0.5f,
                ["AbsorptionScale_Magenta"] = 0.5f,
                ["AbsorptionScale_Yellow"] = 0.5f,
                ["SkyColor_Red"] = 0f,
                ["SkyColor_Green"] = 0f,
                ["SkyColor_Blue"] = 0f,
                ["SkyColor_Alpha"] = 0f,
                ["StartDist"] = 150f,
                ["DirectColor_Red"] = 0.2f,
                ["DirectColor_Green"] = 0.2f,
                ["DirectColor_Blue"] = 0.2f,
                ["DirectColor_Alpha"] = 0.2f,
            },
            [DarknessLevel.High] = new Dictionary<string, float>()
            {
                ["NearDepth"] = 4f,
                //["DrawTiming"] = 2,
                ["FixedDensity"] = 0.35f,
                ["LocalLightScale"] = 0.02f,
                ["AbsorptionScale_Cyan"] = 0.5f,
                ["AbsorptionScale_Magenta"] = 0.5f,
                ["AbsorptionScale_Yellow"] = 0.5f,
                ["SkyColor_Red"] = 0f,
                ["SkyColor_Green"] = 0f,
                ["SkyColor_Blue"] = 0f,
                ["SkyColor_Alpha"] = 0f,
                ["StartDist"] = 150f,
                ["DirectColor_Red"] = 0f,
                ["DirectColor_Green"] = 0f,
                ["DirectColor_Blue"] = 0f,
                ["DirectColor_Alpha"] = 0f,
            },
        };

        static ERHook Hook { get; set; }

        static DarknessLevel CurrentDarknessLevel { get; set; } = DarknessLevel.None;
        const bool doDebugPrint = false;

        static void DebugPrint(string msg)
        {
            if (doDebugPrint)
                Console.WriteLine(msg);
        }

        static string TitleText { get; } = @"

                                  E L D E N   R I N G 
   _____ _    _ _______      _________      __     _        __  __  ____  _____  ______ 
  / ____| |  | |  __ \ \    / /_   _\ \    / /\   | |      |  \/  |/ __ \|  __ \|  ____|
 | (___ | |  | | |__) \ \  / /  | |  \ \  / /  \  | |      | \  / | |  | | |  | | |__   
  \___ \| |  | |  _  / \ \/ /   | |   \ \/ / /\ \ | |      | |\/| | |  | | |  | |  __|  
  ____) | |__| | | \ \  \  /   _| |_   \  / ____ \| |____  | |  | | |__| | |__| | |____ 
 |_____/ \____/|_|  \_\  \/   |_____|   \/_/    \_\______| |_|  |_|\____/|_____/|______|

                                         v1.5
                                    
                                      by Grimrukh
                       
              with special thanks to @JanZielasko, @Thens_DeS, @king_bore_haha

        Keep this companion app running alongside Elden Ring to create the enhanced
        darkness at night. If you don't want darkness, you can simply play without
        running this program. If you ONLY want darkness, make sure you are using the
        modded files from the triple-DISABLED subfolder in `Game (OPTIONS)` in addition 
        to running this app.
";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            //Params.AllVariantsCSVToRegulation();
            //Console.WriteLine("Done.");
            //Console.ReadLine();
            //return;

            // TODO: Testing EMEVD instructions.
            //Dictionary<(int category, int index), List<byte[]>> instructions = new Dictionary<(int, int), List<byte[]>>();
            //foreach (var file in Directory.GetFiles(@"C:\Steam\steamapps\common\ELDEN RING\Game\event"))
            //{
            //    if (!file.EndsWith(".emevd.dcx"))
            //        continue;
            //    var emevd = EMEVD.Read(file);
            //    Console.WriteLine($"Read EMEVD: {file}");
            //    foreach (var evt in emevd.Events)
            //    {
            //        foreach (var instr in evt.Instructions)
            //        {
            //            var tuple = (instr.Bank, instr.ID);
            //            if (!instructions.ContainsKey(tuple))
            //                instructions[tuple] = new List<byte[]>() { instr.ArgData };
            //            else
            //                instructions[tuple].Add(instr.ArgData);
            //        }
            //    }
            //}
            //var instrList = new List<(int cat, int ind)>(instructions.Keys);
            //instrList.Sort();
            //foreach (var instr in instrList)
            //{
            //    Console.WriteLine($"    {instr.cat}, {instr.ind}:");
            //    for (int i = 0; i < Math.Min(10, instructions[instr].Count); i++)
            //    {
            //        string args = BitConverter.ToString(instructions[instr][i]).Replace("-", " ");
            //        Console.WriteLine($"        {args}");
            //    }
            //}                
            //Console.ReadLine();
            //return;

            Console.WriteLine(TitleText);
            
            Hook = new ERHook(5000, 5000);
            Hook.Start();

            Console.WriteLine("\nSearching for running ELDEN RING process...");
            while (!Hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("--> Connected to ELDEN RING successfully.");

            bool lastHasTorch = false;

            while (true)
            {
                if (!Hook.Hooked)
                {
                    CurrentDarknessLevel = DarknessLevel.None;
                    Console.WriteLine("\nLost game connection. Waiting to reconnect...");
                    while (!Hook.Hooked)
                        Thread.Sleep(100);
                    Console.WriteLine("--> Reconnected to ELDEN RING successfully.");
                }

                var (hour, hasTorch) = Hook.GetIngameHourAndTorch();
                DebugPrint($"Current in-game hour, torch: {hour}, {hasTorch}");
                
                // TODO: Check a 'Player Outside' general flag and only set darkness in that case.
                //  I tried this and C#, for some reason, would not show the flag value changing.
                //  I don't actually mind the night darkness in generic dungeons/underground, though.

                if (hour == -1)
                {
                    // Do nothing. No change. (Might want to disable darkness.)
                    DebugPrint("    Time not detected. No change to darkness.");
                }
                else if (5 <= hour && hour < 18)
                {
                    SetDarknessLevel(DarknessLevel.None);
                    DebugPrint("    Darkness level: None");
                }
                else if (hour == 18 || hour == 19)
                {
                    // Low, regardless of whether player has torch.
                    SetDarknessLevel(DarknessLevel.Low, lerpDuration: 10f);
                    DebugPrint("    Darkness level: Low");
                }
                else if (hour == 20 || hour == 21)
                {
                    float lerpDuration = lastHasTorch != hasTorch ? 1f : 3f;
                    if (!hasTorch)
                    {
                        SetDarknessLevel(DarknessLevel.Medium, lerpDuration);
                        DebugPrint("    Darkness level: Medium (No Torch)");
                    }
                    else
                    {
                        SetDarknessLevel(DarknessLevel.Low, lerpDuration);
                        DebugPrint("    Darkness level: Low (Torch)");
                    }
                    
                        
                }
                else if (22 <= hour || hour < 5)
                {
                    float lerpDuration = lastHasTorch != hasTorch ? 1f : 3f;
                    if (!hasTorch)
                    {
                        SetDarknessLevel(DarknessLevel.High, lerpDuration);
                        DebugPrint("    Darkness level: High (No Torch)");
                    }
                    else
                    {
                        SetDarknessLevel(DarknessLevel.Medium, lerpDuration);
                        DebugPrint("    Darkness level: Medium (Torch)");
                    }
                }
                lastHasTorch = hasTorch;
                Thread.Sleep(500);  // 0.5 sec
            }
        }

        static void WaitOneFrame(ref float timer)
        {
            Thread.Sleep(16);
            timer += 0.016f;
        }

        static void LerpDarkness(Dictionary<string, float> startValues, Dictionary<string, float> endValues, float duration = 10f)
        {
            // NOTE: Only keys present in BOTH dictionaries will be used. Other keys will be ignored.
            List<string> sharedKeys = new List<string>();
            foreach (string key in startValues.Keys)
                if (endValues.ContainsKey(key))
                    sharedKeys.Add(key);
            
            Dictionary<string, byte[]> lerpedValues = new Dictionary<string, byte[]>();

            DebugPrint($"Lerping FixedDensity from {startValues["FixedDensity"]} to {endValues["FixedDensity"]}");

            float t = 0f;
            while (t < duration)
            {
                float w = t / duration;

                foreach (string name in sharedKeys)
                {
                    float lerpedValue = Lerp(startValues[name], endValues[name], w);
                    if (name == "FixedDensity")
                        DebugPrint($"   Lerped {name}: {lerpedValue}");
                    lerpedValues[name] = BitConverter.GetBytes(lerpedValue);
                }
                Hook.SetFogValues(lerpedValues);
                WaitOneFrame(ref t);
            }
            DebugPrint("Finished lerp.");
        }

        static void SetDarknessLevel(DarknessLevel level, float lerpDuration = 10f)
        {
            Dictionary<string, float> startValues;
            Dictionary<string, float> targetValues;

            if (level == DarknessLevel.None)
            {
                if (CurrentDarknessLevel == DarknessLevel.None)
                    return;  // nothing to do

                Hook.EnableEldenRingFog();

                startValues = DarknessPresets[CurrentDarknessLevel];
                Dictionary<string, byte[]> targetValuesBytes = Hook.GetFogValues();
                targetValues = new Dictionary<string, float>();
                foreach (KeyValuePair<string, byte[]> kvp in targetValuesBytes)
                    targetValues[kvp.Key] = BitConverter.ToSingle(kvp.Value, 0);

                CurrentDarknessLevel = DarknessLevel.None;  // do not repeat transition

                // Set DrawTiming back to vanilla immediately.
                Hook.SetFogValues(new Dictionary<string, byte[]> { ["DrawTiming"] = targetValuesBytes["DrawTiming"] });
                LerpDarkness(startValues, targetValues, lerpDuration);
                Hook.DisableEldenRingFog();
                return;
            }

            // Will do nothing if already enabled.
            Hook.EnableEldenRingFog();

            targetValues = DarknessPresets[level];

            if (level == CurrentDarknessLevel)
            {
                // Set values directly to target level.
                Dictionary<string, byte[]> currentValues = new Dictionary<string, byte[]>();
                foreach (string name in targetValues.Keys)
                    currentValues[name] = BitConverter.GetBytes(targetValues[name]);

                Hook.SetFogValues(currentValues);
                return;
            }

            if (CurrentDarknessLevel == DarknessLevel.None)
            {
                // Lerp from vanilla values to target values.
                
                CurrentDarknessLevel = level;  // do not repeat transition

                Dictionary<string, byte[]> startValuesBytes = Hook.GetFogValues();
                startValues = new Dictionary<string, float>();
                foreach (KeyValuePair<string, byte[]> kvp in startValuesBytes)
                    startValues[kvp.Key] = BitConverter.ToSingle(kvp.Value, 0);

                Hook.SetFogValues(new Dictionary<string, byte[]> { ["DrawTiming"] = BitConverter.GetBytes(DarknessDrawTiming) });

                LerpDarkness(startValues, targetValues, lerpDuration);
                // Leave injection enabled with final darkness value.
                return;
            }

            // Lerp from current darkness to target darkness (no vanilla involvement).
            startValues = DarknessPresets[CurrentDarknessLevel];
            CurrentDarknessLevel = level;  // do not repeat transition
            LerpDarkness(startValues, targetValues, lerpDuration);
            // Leave injection enabled with final darkness value.
        }

        public static float Lerp(float min, float max, float t)
        {
            return t * (max - min) + min;
        }

        public static float Lerp(float[] minMax, float t)
        {
            return Lerp(minMax[0], minMax[1], t);
        }
    }
}
