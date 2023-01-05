using Erd_Tools;
using static EldenRingSurvival.DebugTools;

namespace EldenRingSurvival
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

        static int DarknessDrawTiming { get; } = 2;  // 'Show VFX'
        static int UpdateIntervalMs { get; } = 400;  // milliseconds between darkness update checks

        static readonly Dictionary<DarknessLevel, Dictionary<string, float>> DarknessPresets = new()
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

        static ErdHook? Hook { get; set; }
        static FogManager? Fog { get; set; }

        static DarknessLevel CurrentDarknessLevel { get; set; } = DarknessLevel.None;
        
        static string TitleText { get; } = @"

                                  E L D E N   R I N G 
   _____ _    _ _______      _________      __     _        __  __  ____  _____  ______ 
  / ____| |  | |  __ \ \    / /_   _\ \    / /\   | |      |  \/  |/ __ \|  __ \|  ____|
 | (___ | |  | | |__) \ \  / /  | |  \ \  / /  \  | |      | \  / | |  | | |  | | |__   
  \___ \| |  | |  _  / \ \/ /   | |   \ \/ / /\ \ | |      | |\/| | |  | | |  | |  __|  
  ____) | |__| | | \ \  \  /   _| |_   \  / ____ \| |____  | |  | | |__| | |__| | |____ 
 |_____/ \____/|_|  \_\  \/   |_____|   \/_/    \_\______| |_|  |_|\____/|_____/|______|

                                         v1.6
                                    
                                      by Grimrukh
                       
              with special thanks to @JanZielasko, @Thens_DeS, @king_bore_haha

                         --- REQUIRES GAME VERSION 1.08.1 ---

        Keep this companion app running alongside Elden Ring to create the enhanced
        darkness at night. If you don't want darkness, you can simply play without
        running this program. If you ONLY want darkness, make sure you are using the
        modded files from the triple-DISABLED subfolder in `Game (OPTIONS)` in addition 
        to running this app.

        This mod requires the usage of free memory inside the game process, the address
        of which is liable to change whenever the game executable is updated (and I
        don't yet trust my tools to automatically find free memory). I will update the
        mod when the game version updates -- if you run it with a different version, it
        will probably crash your game. See the latest compatible version above.

        NOTE: As memory injection is fairly fragile, I highly recommend that you only
        run this program AFTER opening Elden Ring (even just to the main menu), and that
        you close and start a fresh run of this program each time the game process is
        launched. Otherwise, this program may have trouble cleaning up information about
        the previous Elden Ring process and cause the new process to crash on startup.
";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            Console.WriteLine(TitleText);
            
            Hook = new ErdHook(5000, 1000, p => p.MainWindowTitle is "ELDEN RING™" or "ELDEN RING");
            Fog = new FogManager(Hook);
            Hook.Start();

            Console.WriteLine("\nSearching for running ELDEN RING process...");
            while (!Hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("--> Connected to ELDEN RING successfully. Acquiring base address...");
            while (Fog.BaseAddress == null)
                Thread.Sleep(100);
            Console.WriteLine("--> ELDEN RING base address acquired.");

            bool lastHasTorch = false;

            while (true)
            {
                if (!Hook.Hooked)
                {
                    CurrentDarknessLevel = DarknessLevel.None;
                    Console.WriteLine("\nLost game connection. Waiting to reconnect...");
                    while (!Hook.Hooked)
                        Thread.Sleep(100);
                    Console.WriteLine("--> Reconnected to ELDEN RING successfully. Acquiring base address...");
                    while (Fog.BaseAddress == null)
                        Thread.Sleep(100);
                    Console.WriteLine("--> ELDEN RING base address acquired.");
                }

                var (hour, hasTorch, isOutdoors) = Fog.GetIngameHourTorchOutdoors();
                DebugPrint($"Fog injection enabled? {Fog.InjectionEnabled}");
                
                // This carriage-return message is shown only in release build.
                if (!DoDebugPrint)
                {
                    if (hour == -1)
                    {
                        Console.Write($"Hour: ????? | Torch = {hasTorch} | Outdoors = {isOutdoors}        \r");
                    }
                    else
                    {
                        Console.Write($"Hour: {hour:00}:00 | Torch = {hasTorch} | Outdoors = {isOutdoors}        \r");
                    }
                }
                    

                if (hour == -1)
                {
                    //SetDarknessLevel(DarknessLevel.Low, lerpDuration: 10f);

                    // Can't detect hour. Disable darkness injection (or all zeroes may be written).
                    Fog.DisableFogInjection();
                    DebugPrint("    Time not detected. Disabling darkness.");
                }
                else if (!isOutdoors)
                {
                    // No darkness indoors.
                    SetDarknessLevel(DarknessLevel.None);
                    DebugPrint("    Darkness level: None (Indoors)");
                }                
                else if (5 <= hour && hour < 18)
                {
                    SetDarknessLevel(DarknessLevel.None);
                    DebugPrint("    Darkness level: None (Daytime Outdoors)");
                }
                else if (hour == 18 || hour == 19)
                {
                    // Low, regardless of whether player has torch.
                    SetDarknessLevel(DarknessLevel.Low, lerpDuration: 10f);
                    DebugPrint("    Darkness level: Low (Early Evening)");
                }
                else if (hour == 20 || hour == 21)
                {
                    float lerpDuration = lastHasTorch != hasTorch ? 1f : 3f;
                    if (!hasTorch)
                    {
                        SetDarknessLevel(DarknessLevel.Medium, lerpDuration);
                        DebugPrint("    Darkness level: Medium (Mid-Evening, No Torch)");
                    }
                    else
                    {
                        SetDarknessLevel(DarknessLevel.Low, lerpDuration);
                        DebugPrint("    Darkness level: Low (Mid-Evening, Torch)");
                    }
                    
                        
                }
                else if (22 <= hour || hour < 5)
                {
                    float lerpDuration = lastHasTorch != hasTorch ? 1f : 3f;
                    if (!hasTorch)
                    {
                        SetDarknessLevel(DarknessLevel.High, lerpDuration);
                        DebugPrint("    Darkness level: High (Night, No Torch)");
                    }
                    else
                    {
                        SetDarknessLevel(DarknessLevel.Medium, lerpDuration);
                        DebugPrint("    Darkness level: Medium (Night, Torch)");
                    }
                }
                lastHasTorch = hasTorch;
                
                Thread.Sleep(UpdateIntervalMs);
            }
        }

        static void WaitOneFrame(ref float timer)
        {
            Thread.Sleep(16);
            timer += 0.016f;
        }

        static void LerpDarkness(Dictionary<string, float> startValues, Dictionary<string, float> endValues, float duration = 10f)
        {
            if (Fog == null)
            {
                DebugPrint($"FogManager not active. Cannot lerp between darkness levels.");
                return;
            }

            // NOTE: Only keys present in BOTH dictionaries will be used. Other keys will be ignored.
            List<string> sharedKeys = new();
            foreach (string key in startValues.Keys)
                if (endValues.ContainsKey(key))
                    sharedKeys.Add(key);
            
            Dictionary<string, byte[]> lerpedValues = new();

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
                Fog.SetInjectedFogValues(lerpedValues);
                WaitOneFrame(ref t);
            }
            DebugPrint("Finished lerp.");
        }

        static void SetDarknessLevel(DarknessLevel level, float lerpDuration = 10f)
        {
            if (Fog == null)
            {
                DebugPrint("FogManager not active. Cannot set darkness level.");
                return;
            }

            Dictionary<string, float> startValues;
            Dictionary<string, float> targetValues;

            if (level == DarknessLevel.None)
            {
                if (CurrentDarknessLevel == DarknessLevel.None)
                    return;  // nothing to do

                // Will do nothing if injection already enabled.
                Fog.EnableFogInjection();

                startValues = DarknessPresets[CurrentDarknessLevel];
                Dictionary<string, byte[]?>? targetValuesBytes = Fog.GetOriginalFogValues();
                targetValues = new Dictionary<string, float>();
                
                if (targetValuesBytes != null)
                {
                    foreach (KeyValuePair<string, byte[]?> kvp in targetValuesBytes)
                    {
                        if (kvp.Value != null)
                            targetValues[kvp.Key] = BitConverter.ToSingle(kvp.Value, 0);
                    }
                    
                    CurrentDarknessLevel = DarknessLevel.None;  // do not repeat transition

                    // DrawTiming is fixed to original (not lerped).
                    byte[]? drawTiming = targetValuesBytes["DrawTiming"];
                    if (drawTiming != null)
                        Fog.SetInjectedFogValues(new Dictionary<string, byte[]> { ["DrawTiming"] = drawTiming });
                    
                    LerpDarkness(startValues, targetValues, lerpDuration);
                    
                    Fog.DisableFogInjection();
                }
                else
                {
                    Console.WriteLine("ERROR: Could not get original fog values.");
                }
                return;
            }

            // BELOW: Moving to non-None darkness level.

            // Will do nothing if already enabled.
            Fog.EnableFogInjection();

            targetValues = DarknessPresets[level];

            if (level == CurrentDarknessLevel)
            {
                // Set values directly to target level.
                Dictionary<string, byte[]> currentValues = new();
                foreach (string name in targetValues.Keys)
                    currentValues[name] = BitConverter.GetBytes(targetValues[name]);
                Fog.SetInjectedFogValues(currentValues);
                return;
            }

            if (CurrentDarknessLevel == DarknessLevel.None)
            {
                // Lerp from vanilla values to target values.
                
                CurrentDarknessLevel = level;  // do not repeat transition

                Dictionary<string, byte[]?>? startValuesBytes = Fog.GetOriginalFogValues();
                if (startValuesBytes != null)
                {
                    startValues = new Dictionary<string, float>();
                    foreach (KeyValuePair<string, byte[]?> kvp in startValuesBytes)
                    {
                        if (kvp.Value != null)
                            startValues[kvp.Key] = BitConverter.ToSingle(kvp.Value, 0);
                    }

                    // DrawTiming is fixed (not lerped).
                    byte[] drawTiming = BitConverter.GetBytes(DarknessDrawTiming);
                    Fog.SetInjectedFogValues(new Dictionary<string, byte[]> { ["DrawTiming"] = drawTiming });

                    LerpDarkness(startValues, targetValues, lerpDuration);
                    // Leave injection enabled with final darkness value.
                }
                else
                {
                    Console.WriteLine("ERROR: Could not get original fog values.");
                }
                return;
            }

            // Otherwise, lerp from current darkness to target darkness (no vanilla involvement).
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
