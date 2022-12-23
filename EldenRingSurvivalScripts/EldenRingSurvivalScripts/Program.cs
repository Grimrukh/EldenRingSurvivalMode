using SoulsFormats;
using static EldenRingSurvivalScripts.FileUtils;


namespace EldenRingSurvivalScripts
{
    public static class Program
    {
        static void Main()
        {
            //CreateVanillaCSVs();
            CreateModdedVariantRegulations();

            Console.WriteLine("Scripts done. Press Enter to finish.");
            Console.ReadLine();
        }

        static void CreateVanillaCSVs()
        {
            string vanillaRegulationPath = Path.Combine(VANILLA_GAME_PATH, "regulation.bin");
            Params.RegulationToCSV(vanillaRegulationPath, VANILLA_CSV_PATH);
            Console.WriteLine("Created vanilla CSV files.");
        }

        // Python is responsible for converting vanilla CSVs to modded CSVs.

        /// <summary>
        /// Create all `regulation.bin` files for all mod option variants.
        /// </summary>
        static void CreateModdedVariantRegulations()
        {
            Params.AllVariantsCSVToRegulation();
        }

        /// <summary>
        /// Utility script that reports the most common arguments used by each EMEVD instruction type.
        /// 
        /// Note that plenty of zeroes will show up due to event arg replacements.
        /// </summary>
        static void ScanEMEVDInstructionArgs()
        {
            Dictionary<(int category, int index), List<byte[]>> instructions = new();
            foreach (var file in Directory.GetFiles(@"C:\Steam\steamapps\common\ELDEN RING\Game\event"))
            {
                if (!file.EndsWith(".emevd.dcx"))
                    continue;
                EMEVD emevd = EMEVD.Read(file);
                Console.WriteLine($"Read EMEVD: {file}");
                foreach (var evt in emevd.Events)
                {
                    foreach (var instr in evt.Instructions)
                    {
                        var tuple = (instr.Bank, instr.ID);
                        if (!instructions.ContainsKey(tuple))
                            instructions[tuple] = new List<byte[]>() { instr.ArgData };
                        else
                            instructions[tuple].Add(instr.ArgData);
                    }
                }
            }
            var instrList = new List<(int cat, int ind)>(instructions.Keys);
            instrList.Sort();
            foreach (var instr in instrList)
            {
                Console.WriteLine($"    {instr.cat}, {instr.ind}:");
                for (int i = 0; i < Math.Min(10, instructions[instr].Count); i++)
                {
                    string args = BitConverter.ToString(instructions[instr][i]).Replace("-", " ");
                    Console.WriteLine($"        {args}");
                }
            }
        }
    }
}

