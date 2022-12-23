using System.IO;

namespace EldenRingSurvivalMode
{
    /// <summary>
    /// Basic utilities for creating/modifying files.
    /// </summary>
    internal static class FileUtils
    {
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
