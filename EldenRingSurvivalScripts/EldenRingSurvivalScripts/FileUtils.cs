
namespace EldenRingSurvivalScripts
{
    /// <summary>
    /// Basic utilities for creating/modifying files.
    /// </summary>
    internal static class FileUtils
    {
        public const string VANILLA_CSV_PATH = @"C:\Dark Souls\Projects\EldenRingSurvivalMode\EldenRingSurvivalScripts\EldenRingSurvivalScripts\Vanilla CSV";
        public const string MODDED_CSV_PATH = @"C:\Dark Souls\Projects\EldenRingSurvivalMode\EldenRingSurvivalScripts\EldenRingSurvivalScripts\Modded CSV";
        public const string MOD_DIST_OPTIONS_PATH = @"C:\Dark Souls\Projects\EldenRingSurvivalMode\dist\Game (OPTIONS)";
        public const string VANILLA_GAME_PATH = @"C:\Steam\steamapps\common\ELDEN RING (Vanilla 1.08)\Game";
        public const string PARAMDEFS_PATH = @"C:\Dark Souls\Projects\EldenRingSurvivalMode\Dependencies\Paramdex\ER\Defs";

        public static void CreateBak(string path)
        {
            string bakPath = path.EndsWith(".bak") ? path : path + ".bak";
            if (!File.Exists(bakPath))
                File.Copy(path, bakPath);
        }

        public static void RestoreBak(string path)
        {
            string bakPath = path.EndsWith(".bak") ? path : path + ".bak";
            if (File.Exists(bakPath))
                File.Copy(bakPath, path, overwrite: true);
        }
    }
}
