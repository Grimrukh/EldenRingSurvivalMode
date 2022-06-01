using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Text.RegularExpressions;
using System.Threading;
using SoulsFormats;
using EldenRingSurvivalMode.GameHook;

namespace EldenRingSurvivalMode
{
    internal class Program
    {
        const string ERPath = @"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game";
        const bool doPrint = false;

        static Dictionary<string, object[]> DarknessPresets = new Dictionary<string, object[]>()
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

        static void CreateBak(string path)
        {
            string bakPath = path.EndsWith(".bak") ? path : path + ".bak";
            if (!File.Exists(bakPath))
                File.Copy(path, bakPath);
        }

        static void RestoreBak(string path)
        {
            string bakPath = path.EndsWith(".bak") ? path : path + ".bak";
            if (File.Exists(bakPath))
                File.Copy(bakPath, path, overwrite: true);
        }

        static void DarkenLightSet(string gparamPath)
        {
            CreateBak(gparamPath);
            RestoreBak(gparamPath);

            GPARAM gparam = GPARAM.Read(gparamPath);
            Console.WriteLine($"Read GPARAM successfully: {gparamPath}");

            GPARAM.Group lightSet = gparam.Groups[0];
            foreach (var param in lightSet.Params)
            {
                //Console.WriteLine($"    {param.Name1} | {param.Name2} | {param.Type}");
                if (param.Type == GPARAM.ParamType.Float4)
                {
                    // Nuke.
                    for (int v = 0; v < param.Values.Count; v++)
                    {
                        param.Values[v] = Vector4.One;
                    }
                }
            }
            
            gparam.Write(gparamPath);
            Console.WriteLine($"Wrote GPARAM successfully: {Path.GetFileName(gparamPath)}");
        }

        static void EditFog(string gparamPath)
        {
            // Open GPARAM and nuke all fog values in it for testing purposes.
            CreateBak(gparamPath);
            RestoreBak(gparamPath);
            
            GPARAM gparam = GPARAM.Read(gparamPath);
            Console.WriteLine($"Read GPARAM successfully: {gparamPath}");

            GPARAM.Group fog = gparam.Groups.Where(x => x.Name1.Contains("VolumetricFog")).First();

            for (int i = 0; i < fog.Params.Count; i++)
            {
                var param = fog.Params[i];

                if (doPrint)
                {
                    Console.WriteLine($"Param: {param.Name1} | {param.Name2} (type {param.Type})");
                    Console.WriteLine($"    {param.Values.Count} values: {string.Join(", ", param.Values)}");
                }

                if (DarknessPresets.ContainsKey(param.Name2))
                {
                    // TODO: Try modifying only 'night' values.
                    for (int v = 0; v < param.Values.Count; v++)
                    {
                        param.Values[v] = DarknessPresets[param.Name2];
                    }
                    //Console.WriteLine($"Replaced {param.Name2} with JZ Preset: {JZPreset[param.Name2]}");
                }
            }

            gparam.Write(gparamPath);
            Console.WriteLine($"Wrote GPARAM successfully: {Path.GetFileName(gparamPath)}");
            //Console.ReadLine();
        }

        static void NukeFloatParam(GPARAM.Param param)
        {
            if (param.Type == GPARAM.ParamType.Float)
            {
                for (int v = 0; v < param.Values.Count; v++)
                {
                    // Zero float.
                    param.Values[v] = 0f;
                }
            }
        }

        static List<string> NightGparamNames = new List<string>
        {
            "m00_00_0020_weatheroutdoor.gparam.dcx",  // Limgrave (West)
            "m00_00_0621_weatheroutdoor.gparam.dcx",  // Liurnia (Lakes)
            "m00_00_0622_weatheroutdoor.gparam.dcx",  // Liurnia (Caria Manor)
            "m60_00_0010.gparam.dcx",  // Liurnia
            "m60_00_0020.gparam.dcx",  // Altus
            "m60_00_0021.gparam.dcx",  // Mt. Gelmir
            "m00_00_0050_weatheroutdoor.gparam.dcx",  // Altus (Windmills)
            "m00_00_0051_weatheroutdoor.gparam.dcx",  // Altus (Bower Woods)
        };

        void DrawParamStuff()
        {
            string drawparamPath = Path.Combine(ERPath, @"param\drawparam\");

            Regex allRegex = new Regex(@".*\.gparam\.dcx$");
            Regex weatherRegex = new Regex(@"m00.*weatheroutdoor\.gparam\.dcx$");
            Regex overworldRegex = new Regex(@"m60.*\.gparam\.dcx$");

            //Regex exactRegex = new Regex(@"m00.*_06\d\d_weatheroutdoor\.gparam\.dcx$");
            Regex exactRegex = new Regex(@"m60_00_0010\.gparam\.dcx$");

            bool doNuke(string p)
            {
                //if (NightGparamNames.Contains(Path.GetFileName(p)))
                //    return true;
                //return exactRegex.IsMatch(p);
                return false;
            }

            foreach (string path in Directory.GetFiles(drawparamPath).Where(x => allRegex.IsMatch(x)))
            {
                if (doNuke(path))
                    EditFog(path);
                //DarkenLightSet(path);
                else  // just restore vanilla
                    RestoreBak(path);
            }
        }

        static ERHook Hook { get; set; }

        static void DebugPrint(string msg)
        {
            if (doPrint)
                Console.WriteLine(msg);
        }

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            Console.WriteLine("ELDEN RING SURVIVAL MODE: COMPANION APP (v1.0)");
            Console.WriteLine("    by Grimrukh\n");
            Console.WriteLine("Keep this executable running alongside Elden Ring. It manages darkness effects at night.");
            Console.WriteLine("If you have any issues with this executable, you can always play the mod without darkness!\n");

            Hook = new ERHook(5000, 5000);
            Hook.Start();

            Console.WriteLine("Waiting for game application to open...");
            while (!Hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("Hooked.");

            while (true)
            {
                int hour = Hook.GetIngameHour();
                DebugPrint($"Current in-game hour: {hour}");
                // TODO: Check a 'Player Outside' general flag and only set darkness in that case.
                // TODO: Functions to smoothly Lerp from one darkness level to the next?
                if (hour == -1)
                {
                    // Do nothing. No change. (Might want to disable darkness.)
                    DebugPrint("No hour, so no change.");
                }
                else if ( 7 <= hour && hour < 18)
                {
                    // No night effects.
                    Hook.DisableEldenRingFog();
                    DebugPrint("Disabling darkness.");
                }
                else if (hour == 18 || hour == 6)
                {
                    // Mild darkness.
                    Hook.EnableEldenRingFog();
                    SetFogPreset(0);
                    DebugPrint("Darkness level 0.");
                }
                else if (hour == 19 || hour == 5)
                {
                    // Moderate darkness.
                    Hook.EnableEldenRingFog();
                    SetFogPreset(1);
                    Console.WriteLine("Darkness level 1.");
                }
                else if (20 <= hour || hour < 5)
                {
                    // Max darkness.
                    Hook.EnableEldenRingFog();
                    SetFogPreset(2);
                    DebugPrint("Darkness level 2.");
                }
                Thread.Sleep(1000);
            }
        }

        public static void SetFogPreset(int level)
        {
            // Set fog values ONCE to preset level.
            Vector3 absorptionScale = (Vector3)DarknessPresets["AbsorptionScale"][level];
            Vector4 skyColor = (Vector4)DarknessPresets["SkyColor"][level];
            Vector4 directColor = (Vector4)DarknessPresets["DirectColor"][level];
            
            Hook.SetFogValues(
                BitConverter.GetBytes((float)DarknessPresets["NearDepth"][level]),
                BitConverter.GetBytes((int)DarknessPresets["DrawTiming"][level]),
                BitConverter.GetBytes((float)DarknessPresets["FixedDensity"][level]),
                BitConverter.GetBytes((float)DarknessPresets["LocalLightScale"][level]),
                BitConverter.GetBytes(absorptionScale.X),
                BitConverter.GetBytes(absorptionScale.Y),
                BitConverter.GetBytes(absorptionScale.Z),
                BitConverter.GetBytes(skyColor.X),
                BitConverter.GetBytes(skyColor.Y),
                BitConverter.GetBytes(skyColor.Z),
                BitConverter.GetBytes(skyColor.W),
                BitConverter.GetBytes((float)DarknessPresets["StartDist"][level]),
                BitConverter.GetBytes(directColor.X),
                BitConverter.GetBytes(directColor.Y),
                BitConverter.GetBytes(directColor.Z),
                BitConverter.GetBytes(directColor.W)
            );
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
