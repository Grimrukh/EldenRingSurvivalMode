using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingSurvivalMode
{
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
