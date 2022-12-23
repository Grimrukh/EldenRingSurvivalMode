using SoulsFormats;
using static EldenRingSurvivalScripts.FileUtils;

namespace EldenRingSurvivalScripts
{
    internal static class Params
    {
        /// <summary>
        /// Loads a single `PARAM.Row` representation from one row of a PARAM CSV file.
        /// </summary>
        class CSVRow
        {
            public int ID { get; }
            public string Name { get; }
            public List<string> Values { get; }

            public CSVRow(string csvLine, char separator = ';')
            {
                csvLine = csvLine.TrimEnd(separator);
                string[] values = csvLine.Split(separator);
                ID = int.Parse(values[0]);
                Name = values[1];
                Values = new List<string>();
                for (int i = 2; i < values.Length; i++)
                    Values.Add(values[i]);
            }

            /// <summary>
            /// Create a `CSVRow` directly from a `PARAM.Row`, rather than a text file.
            /// </summary>
            /// <param name="row"></param>
            /// <returns></returns>
            public CSVRow(PARAM.Row row)
            {
                ID = row.ID;
                Name = row.Name;
                Values = new List<string>();
                List<PARAM.Cell> nonPadCells = row.Cells.Where(cell => cell.Def.DisplayType != PARAMDEF.DefType.dummy8).ToList();
                foreach (var cell in nonPadCells)
                {
                    string? valueString = cell.Value.ToString();
                    if (valueString == null)
                        throw new ArgumentException($"Could not convert null PARAM field to string for `CSVRow`: {cell.Def.InternalName}");
                    Values.Add(valueString);
                }
            }

            /// <summary>
            /// Convert CSV row to a write-ready CSV file line.
            /// </summary>
            /// <param name="separator"></param>
            /// <returns></returns>
            public string ToTextLine(char separator = ';')
            {
                string valuesString = string.Join(separator, Values.ToArray());
                return string.Join(separator, ID.ToString(), Name, valuesString);
            }

            public void ApplyToRow(PARAM.Row row)
            {
                row.ID = ID;
                row.Name = Name;

                List<PARAM.Cell> nonPadCells = row.Cells.Where(cell => cell.Def.DisplayType != PARAMDEF.DefType.dummy8).ToList();
                if (nonPadCells.Count != Values.Count)
                {
                    Console.WriteLine("Non-padding cells:");
                    foreach (var cell in nonPadCells)
                    {
                        Console.WriteLine($"    {cell.Def.InternalName} | {cell.Def.InternalType}");
                    }
                    //foreach (var value in Values)
                    //{
                    //    Console.WriteLine($"    Value: {value}");
                    //}
                    throw new Exception($"Number of CSV cells ({Values.Count}) does not match number of non-padding PARAM cells ({nonPadCells.Count})");
                }
                    
                for (int i = 0; i < Values.Count; i++)
                    nonPadCells[i].Value = Values[i];  // `SoulsFormats` will convert string to appropriate type automatically
            }

            public static void ApplyAllRows(IEnumerable<CSVRow> rows, PARAM param)
            {
                int csvRowCount = rows.Count();
                int currentParamRowsCount = param.Rows.Count;
                if (currentParamRowsCount < csvRowCount)
                {
                    // Add default PARAM rows to catch up.
                    for (int i = 0; i < csvRowCount - currentParamRowsCount; i++)
                    {
                        PARAM.Row newRow = new(-1, "", param.AppliedParamdef);
                        param.Rows.Add(newRow);
                    }
                }
                else if (csvRowCount < param.Rows.Count)
                {
                    // Delete PARAM rows.
                    param.Rows = param.Rows.GetRange(0, csvRowCount);
                }

                int rowIndex = 0;
                foreach (CSVRow row in rows)
                {
                    PARAM.Row paramRow = param.Rows[rowIndex++];
                    row.ApplyToRow(paramRow);
                }
            }
        }


        static Dictionary<string, string> Modes { get; } = new Dictionary<string, string>
        {
            ["Survival"] = @"Survival ENABLED\Weapon Tree DISABLED\Diseases DISABLED",
            ["Weapons"] = @"Survival DISABLED\Weapon Tree ENABLED\Diseases DISABLED",
            ["Diseases"] = @"Survival DISABLED\Weapon Tree DISABLED\Diseases ENABLED",
            ["Survival_Weapons"] = @"Survival ENABLED\Weapon Tree ENABLED\Diseases DISABLED",
            ["Survival_Diseases"] = @"Survival ENABLED\Weapon Tree DISABLED\Diseases ENABLED",
            ["Weapons_Diseases"] = @"Survival DISABLED\Weapon Tree ENABLED\Diseases ENABLED",
            ["Survival_Weapons_Diseases"] = @"Survival ENABLED\Weapon Tree ENABLED\Diseases ENABLED",
        };

        /// <summary>
        /// Convert `regulation.bin` file into a directory of CSV files
        /// in the same basic format as exported Yapped CSV rows:
        ///     `Row ID;Row Name;Value1;Value2;Value3;...`
        /// </summary>
        /// <param name="regulationPath"></param>
        /// <param name="csvDirectory"></param>
        public static void RegulationToCSV(string regulationPath, string csvDirectory)
        {
            BND4 parambnd = SFUtil.DecryptERRegulation(regulationPath);
            List<PARAMDEF> paramdefs = LoadParamdefs(PARAMDEFS_PATH);
            char separator = ';';

            if (!Directory.Exists(csvDirectory))
                Directory.CreateDirectory(csvDirectory);

            foreach (BinderFile paramFile in parambnd.Files)
            {
                string paramName = Path.GetFileNameWithoutExtension(paramFile.Name);
                string csvPath = Path.Combine(csvDirectory, paramName + ".csv");

                PARAM param = PARAM.Read(paramFile.Bytes);
                bool applied = param.ApplyParamdefCarefully(paramdefs);
                if (!applied)
                {
                    Console.WriteLine($"WARNING: No Paramdefs found for param file {paramName}. No CSV generated.");
                    continue;
                }

                List<string> fieldNames = param.AppliedParamdef.Fields
                    .Where(field => field.DisplayType != PARAMDEF.DefType.dummy8)
                    .Select(field => field.InternalName).ToList();
                string fieldNamesString = string.Join(separator, fieldNames);

                // Get CSV row lines.
                List<string> csvRows = new()
                {
                    string.Join(separator, "Row ID", "Row Name", fieldNamesString)  // header
                };
                foreach (PARAM.Row row in param.Rows)
                    csvRows.Add(new CSVRow(row).ToTextLine());

                string csvText = string.Join('\n', csvRows) + "\n";  // note final newline

                File.WriteAllText(csvPath, csvText);
            }
        }

        /// <summary>
        /// Convert Yapped CSV files (generated by my Python code) into
        /// `regulation.bin` files for play.
        /// 
        /// This function only serves to remove Yapped from the equation
        /// for now, rather than functioning as an actual new installer
        /// (since Python is still required). 
        /// </summary>
        public static void CSVToRegulation(string csvDirectory, string regulationPath, string vanillaRegulationPath)
        {
            if (!File.Exists(vanillaRegulationPath))
                throw new Exception($"Could not find `vanillaRegulationPath`: {vanillaRegulationPath}");

            // Start with this vanilla regulation, which we will modify with the CSVs.
            BND4 parambnd = SFUtil.DecryptERRegulation(vanillaRegulationPath);

            List<PARAMDEF> paramdefs = LoadParamdefs(PARAMDEFS_PATH);

            foreach (string csvFile in Directory.GetFiles(csvDirectory))
            {
                string fileName = Path.GetFileName(csvFile);
                if (!fileName.EndsWith(".csv"))
                    continue;
                string paramName = Path.GetFileNameWithoutExtension(fileName);
                BinderFile paramFile = parambnd.Files.Where(x => x.Name == $@"N:\GR\data\Param\param\GameParam\{paramName}.param").First();
                PARAM param = PARAM.Read(paramFile.Bytes);
                param.ApplyParamdefCarefully(paramdefs);
                List<CSVRow> paramCSV = LoadParamCSV(csvFile);
                CSVRow.ApplyAllRows(paramCSV, param);
                paramFile.Bytes = param.Write();
            }

            SFUtil.EncryptERRegulation(regulationPath, parambnd);
        }

        public static void AllVariantsCSVToRegulation()
        {
            string vanillaRegulationPath = Path.Combine(VANILLA_GAME_PATH, "regulation.bin");

            foreach (KeyValuePair<string, string> kvp in Modes)
            {
                string csvSubdir = kvp.Key;
                string distSubdir = kvp.Value;
                string modModeCSVPath = Path.Combine(MODDED_CSV_PATH, csvSubdir);
                string modModeRegulationPath = Path.Combine(MOD_DIST_OPTIONS_PATH, distSubdir, "regulation.bin");
                CSVToRegulation(modModeCSVPath, modModeRegulationPath, vanillaRegulationPath);
                Console.WriteLine($"Saved `regulation.bin` for variant: {csvSubdir}");
            }
        }

        /// <summary>
        /// Load ParamDefs from Paramdex XMLs.
        /// </summary>
        /// <returns></returns>
        static List<PARAMDEF> LoadParamdefs(string defsDirectory)
        {
            List<PARAMDEF> defs = new();
            foreach (string file in Directory.GetFiles(defsDirectory))
            {
                PARAMDEF paramdef = PARAMDEF.XmlDeserialize(file);
                defs.Add(paramdef);
            }
            return defs;
        }

        /// <summary>
        /// Read a Yapped CSV into a list of PARAM rows (which are each a list of string values).
        /// 
        /// Each row starts with its ID, then Name, then its non-padding values.
        /// </summary>
        /// <param name="csvPath"></param>
        /// <returns></returns>
        static List<CSVRow> LoadParamCSV(string csvPath)
        {
            List<CSVRow> rows = new();
            bool headerRead = false;
            foreach (string line in File.ReadLines(csvPath))
            {
                if (!headerRead)
                {
                    string[] header = line.Split(';');
                    headerRead = true;
                    continue;
                }
                rows.Add(new CSVRow(line));
            }
            return rows;
        }
    }
}
