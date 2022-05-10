using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using SoulsFormats;
using EldenRingSurvivalMode.GameHook;

namespace EldenRingSurvivalMode
{
    internal class Program
    {
        static string ERPath = @"C:\Steam\steamapps\common\ELDEN RING (Modding)\Game";

        [STAThread]
        static void Main()
        {
            Thread.CurrentThread.CurrentCulture = new System.Globalization.CultureInfo("en-US");

            ERHook hook = new ERHook(5000, 5000);
            hook.Start();

            Console.WriteLine("Waiting for game application to open...");
            while (!hook.Hooked)
                Thread.Sleep(100);
            Console.WriteLine("Hooked.");

            float t = 0;  // parameterizes min to max
            float[] startMultiplier = new float[] { 1f, 1.5f };
            float[] densityNear = new float[] { 0.001f, 0.25f };
            float[] alpha = new float[] { 1f, 0f };
            while (true)
            {
                // Alternate fog values between midday/midnight every 2 seconds.
                float w = 0.5f + 0.5f * (float)Math.Sin(10 * t / (2 * Math.PI));
                hook.SetFogValues(Lerp(startMultiplier, w), Lerp(densityNear, w), Lerp(alpha, w));
                Thread.Sleep(16);
                t += 0.016f;
            }

            Console.WriteLine("Done.");
            Console.ReadLine();
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
