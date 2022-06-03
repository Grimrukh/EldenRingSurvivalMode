using System;
using System.Collections.Generic;
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

        static readonly Dictionary<string, object[]> DarknessPresets = new Dictionary<string, object[]>()
        {
            ["NearDepth"] = new object[] { 10f, 8f, 4f },  // distance from player marked as 'near'
            ["DrawTiming"] = new object[] { 2, 2, 2 },  // Show VFX
            ["FixedDensity"] = new object[] { 0.1f, 0.2f, 0.6f },  // higher values bring in fog closer to player
            ["LocalLightScale"] = new object[] { 0.02f, 0.02f, 0.02f },
            ["AbsorptionScale"] = new object[] { new Vector3(0.5f, 0.5f, 0.5f), new Vector3(0.5f, 0.5f, 0.5f), new Vector3(0.5f, 0.5f, 0.5f) },
            ["SkyColor"] = new object[] { new Vector4(0f, 0f, 0f, 0f), new Vector4(0f, 0f, 0f, 0f), new Vector4(0f, 0f, 0f, 0f) },
            ["StartDist"] = new object[] { 150f, 150f, 150f },
            ["DirectColor"] = new object[] { new Vector4(0.4f, 0.4f, 0.4f, 0.4f), new Vector4(0.2f, 0.2f, 0.2f, 0.2f), new Vector4(0f, 0f, 0f, 0f) },
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

                                         v1.0
                                    
                                      by Grimrukh
                       
              with special thanks to @JanZielasko, @Thens_DeS, @king_bore_haha

        Keep this companion app running alongside Elden Ring to create the enhanced
        darkness at night. If you don't want darkness, you can simply play without
        running this program. If you ONLY want darkness, make sure you are using the
        modded files from `Game (Darkness Only)` in addition to running this app.
";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            Console.WriteLine(TitleText);
            
            Hook = new ERHook(5000, 5000);
            Hook.Start();

            Console.WriteLine("\nSearching for running ELDEN RING process...");
            while (!Hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("--> Connected to ELDEN RING successfully.");

            while (true)
            {
                if (!Hook.Hooked)
                {
                    Console.WriteLine("\nLost game connection. Waiting to reconnect...");
                    while (!Hook.Hooked)
                        Thread.Sleep(100);
                    Console.WriteLine("--> Reconnected to ELDEN RING successfully.");
                }

                int hour = Hook.GetIngameHour();
                DebugPrint($"Current in-game hour: {hour}");
                
                // TODO: Check a 'Player Outside' general flag and only set darkness in that case.
                //  I tried this and C#, for some reason, would not show the flag value changing.
                //  I don't actually mind the night darkness in generic dungeons/underground, though.

                if (hour == -1)
                {
                    // Do nothing. No change. (Might want to disable darkness.)
                    DebugPrint("    Time not detected. No change to darkness.");
                }
                else if ( 7 <= hour && hour < 19)
                {
                    SetDarknessLevel(DarknessLevel.None);
                    DebugPrint("    Darkness level: None");
                    CurrentDarknessLevel = DarknessLevel.None;
                }
                else if (hour == 19 || hour == 6)
                {
                    SetDarknessLevel(DarknessLevel.Low);
                    DebugPrint("    Darkness level: Low");
                }
                else if (hour == 20 || hour == 5)
                {
                    SetDarknessLevel(DarknessLevel.Medium);
                    DebugPrint("    Darkness level: Medium");
                }
                else if (21 <= hour || hour < 5)
                {
                    SetDarknessLevel(DarknessLevel.High);
                    DebugPrint("    Darkness level: High");
                }
                Thread.Sleep(3000);  // 3 sec
            }
        }

        static void SetDarknessLevel(DarknessLevel level, float lerpDuration = 10f)
        {
            float t = 0;

            if (level == DarknessLevel.None)
            {
                if (CurrentDarknessLevel == DarknessLevel.None)
                    return;  // nothing to do

                Hook.EnableEldenRingFog();

                // Disable fog by lerping density down to zero, then disabling the injection.
                float startNearDepth = (float)DarknessPresets["NearDepth"][(int)CurrentDarknessLevel];
                int startDrawTiming = (int)DarknessPresets["DrawTiming"][(int)CurrentDarknessLevel];
                float startFixedDensity = (float)DarknessPresets["FixedDensity"][(int)CurrentDarknessLevel];
                float startLocalLightScale = (float)DarknessPresets["LocalLightScale"][(int)CurrentDarknessLevel];
                Vector3 startAbsorptionScale = (Vector3)DarknessPresets["AbsorptionScale"][(int)CurrentDarknessLevel];
                Vector4 startSkyColor = (Vector4)DarknessPresets["SkyColor"][(int)CurrentDarknessLevel];
                float startStartDist = (float)DarknessPresets["StartDist"][(int)CurrentDarknessLevel];
                Vector4 startDirectColor = (Vector4)DarknessPresets["DirectColor"][(int)CurrentDarknessLevel];

                CurrentDarknessLevel = DarknessLevel.None;  // do not repeat transition

                while (t < lerpDuration)
                {
                    float w = t / lerpDuration;
                    Hook.SetFogValues(
                        BitConverter.GetBytes(startNearDepth),
                        BitConverter.GetBytes(startDrawTiming),
                        BitConverter.GetBytes(Lerp(startFixedDensity, 0f, w)),
                        BitConverter.GetBytes(startLocalLightScale),
                        BitConverter.GetBytes(startAbsorptionScale.X),
                        BitConverter.GetBytes(startAbsorptionScale.Y),
                        BitConverter.GetBytes(startAbsorptionScale.Z),
                        BitConverter.GetBytes(startSkyColor.X),
                        BitConverter.GetBytes(startSkyColor.Y),
                        BitConverter.GetBytes(startSkyColor.Z),
                        BitConverter.GetBytes(startSkyColor.W),
                        BitConverter.GetBytes(startStartDist),
                        BitConverter.GetBytes(startDirectColor.X),
                        BitConverter.GetBytes(startDirectColor.Y),
                        BitConverter.GetBytes(startDirectColor.Z),
                        BitConverter.GetBytes(startDirectColor.W)
                    );
                    // Sleep for one frame (at 60 FPS).
                    Thread.Sleep(16);
                    t += 0.016f;
                }
                Hook.DisableEldenRingFog();
                return;
            }

            // Will do nothing if already enabled.
            Hook.EnableEldenRingFog();

            float targetNearDepth = (float)DarknessPresets["NearDepth"][(int)level];
            int targetDrawTiming = (int)DarknessPresets["DrawTiming"][(int)level];
            float targetFixedDensity = (float)DarknessPresets["FixedDensity"][(int)level];
            float targetLocalLightScale = (float)DarknessPresets["LocalLightScale"][(int)level];
            Vector3 targetAbsorptionScale = (Vector3)DarknessPresets["AbsorptionScale"][(int)level];
            Vector4 targetSkyColor = (Vector4)DarknessPresets["SkyColor"][(int)level];
            float targetStartDist = (float)DarknessPresets["StartDist"][(int)level];
            Vector4 targetDirectColor = (Vector4)DarknessPresets["DirectColor"][(int)level];

            if (level == CurrentDarknessLevel)
            {
                // Set values directly to target level.
                Hook.SetFogValues(
                    BitConverter.GetBytes(targetNearDepth),
                    BitConverter.GetBytes(targetDrawTiming),
                    BitConverter.GetBytes(targetFixedDensity),
                    BitConverter.GetBytes(targetLocalLightScale),
                    BitConverter.GetBytes(targetAbsorptionScale.X),
                    BitConverter.GetBytes(targetAbsorptionScale.Y),
                    BitConverter.GetBytes(targetAbsorptionScale.Z),
                    BitConverter.GetBytes(targetSkyColor.X),
                    BitConverter.GetBytes(targetSkyColor.Y),
                    BitConverter.GetBytes(targetSkyColor.Z),
                    BitConverter.GetBytes(targetSkyColor.W),
                    BitConverter.GetBytes(targetStartDist),
                    BitConverter.GetBytes(targetDirectColor.X),
                    BitConverter.GetBytes(targetDirectColor.Y),
                    BitConverter.GetBytes(targetDirectColor.Z),
                    BitConverter.GetBytes(targetDirectColor.W)
                );
            }
            else
            {
                if (CurrentDarknessLevel == DarknessLevel.None)
                {
                    // Set values directly to target level EXCEPT for density, which is lerped in from zero.

                    CurrentDarknessLevel = level;  // do not repeat transition
                    
                    while (t < lerpDuration)
                    {
                        float w = t / lerpDuration;
                        Hook.SetFogValues(
                            BitConverter.GetBytes(targetNearDepth),
                            BitConverter.GetBytes(targetDrawTiming),
                            BitConverter.GetBytes(Lerp(0f, targetFixedDensity, w)),
                            BitConverter.GetBytes(targetLocalLightScale),
                            BitConverter.GetBytes(targetAbsorptionScale.X),
                            BitConverter.GetBytes(targetAbsorptionScale.Y),
                            BitConverter.GetBytes(targetAbsorptionScale.Z),
                            BitConverter.GetBytes(targetSkyColor.X),
                            BitConverter.GetBytes(targetSkyColor.Y),
                            BitConverter.GetBytes(targetSkyColor.Z),
                            BitConverter.GetBytes(targetSkyColor.W),
                            BitConverter.GetBytes(targetStartDist),
                            BitConverter.GetBytes(targetDirectColor.X),
                            BitConverter.GetBytes(targetDirectColor.Y),
                            BitConverter.GetBytes(targetDirectColor.Z),
                            BitConverter.GetBytes(targetDirectColor.W)
                        );
                        // Sleep for one frame (at 60 FPS).
                        Thread.Sleep(16);
                        t += 0.016f;
                    }
                }
                else
                {
                    // Lerp ALL values from current level to target level.
                    float startNearDepth = (float)DarknessPresets["NearDepth"][(int)CurrentDarknessLevel];
                    int startDrawTiming = (int)DarknessPresets["DrawTiming"][(int)CurrentDarknessLevel];
                    float startFixedDensity = (float)DarknessPresets["FixedDensity"][(int)CurrentDarknessLevel];
                    float startLocalLightScale = (float)DarknessPresets["LocalLightScale"][(int)CurrentDarknessLevel];
                    Vector3 startAbsorptionScale = (Vector3)DarknessPresets["AbsorptionScale"][(int)CurrentDarknessLevel];
                    Vector4 startSkyColor = (Vector4)DarknessPresets["SkyColor"][(int)CurrentDarknessLevel];
                    float startStartDist = (float)DarknessPresets["StartDist"][(int)CurrentDarknessLevel];
                    Vector4 startDirectColor = (Vector4)DarknessPresets["DirectColor"][(int)CurrentDarknessLevel];

                    CurrentDarknessLevel = level;  // do not repeat transition

                    while (t < lerpDuration)
                    {
                        float w = t / lerpDuration;

                        Hook.SetFogValues(
                            BitConverter.GetBytes(Lerp(startNearDepth, targetNearDepth, w)),
                            BitConverter.GetBytes(Lerp(startDrawTiming, targetDrawTiming, w)),
                            BitConverter.GetBytes(Lerp(startFixedDensity, targetFixedDensity, w)),
                            BitConverter.GetBytes(Lerp(startLocalLightScale, targetLocalLightScale, w)),
                            BitConverter.GetBytes(Lerp(startAbsorptionScale.X, targetAbsorptionScale.X, w)),
                            BitConverter.GetBytes(Lerp(startAbsorptionScale.Y, targetAbsorptionScale.Y, w)),
                            BitConverter.GetBytes(Lerp(startAbsorptionScale.Z, targetAbsorptionScale.Z, w)),
                            BitConverter.GetBytes(Lerp(startSkyColor.X, targetSkyColor.X, w)),
                            BitConverter.GetBytes(Lerp(startSkyColor.Y, targetSkyColor.Y, w)),
                            BitConverter.GetBytes(Lerp(startSkyColor.Z, targetSkyColor.Z, w)),
                            BitConverter.GetBytes(Lerp(startSkyColor.W, targetSkyColor.W, w)),
                            BitConverter.GetBytes(Lerp(startStartDist, targetStartDist, w)),
                            BitConverter.GetBytes(Lerp(startDirectColor.X, targetDirectColor.X, w)),
                            BitConverter.GetBytes(Lerp(startDirectColor.Y, targetDirectColor.Y, w)),
                            BitConverter.GetBytes(Lerp(startDirectColor.Z, targetDirectColor.Z, w)),
                            BitConverter.GetBytes(Lerp(startDirectColor.W, targetDirectColor.W, w))
                        );

                        // Sleep for one frame (at 60 FPS).
                        Thread.Sleep(16);
                        t += 0.016f;
                    }
                }                
            }            
        }

        public static void TestFog(ERHook hook)
        {
            float t = 0;  // parameterizes min to max
            float period = 10f;

            float[] nearDepthRange = new float[] { 1f, 4f };
            float[] fixedDensityRange = new float[] { 0.02f, 0.6f };
            float[] directColorAlphaRange = new float[] { 0.2f, 0f };
            
            while (true)
            {
                // Alternate fog values between midday/midnight every `period` seconds.
                float w = 0.5f + 0.5f * (float)Math.Sin(period * t / (2 * Math.PI));
                float nearDepth = Lerp(nearDepthRange, w);
                float fixedDensity = Lerp(fixedDensityRange, w);
                float directColorAlpha = Lerp(directColorAlphaRange, w);
                hook.SetFogValues(
                    BitConverter.GetBytes(nearDepth),
                    //BitConverter.GetBytes(2),  // DrawTiming constant
                    BitConverter.GetBytes(fixedDensity),
                    //BitConverter.GetBytes(0.02f),  // LocalLightScale constant
                    BitConverter.GetBytes(directColorAlpha),  // as SkyColor_Alpha
                    BitConverter.GetBytes(directColorAlpha)
                );
                Thread.Sleep(16);
                t += 0.016f;
            }
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
