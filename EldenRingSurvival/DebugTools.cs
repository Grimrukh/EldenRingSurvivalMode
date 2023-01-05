namespace EldenRingSurvival
{
    public static class DebugTools
    {
        public static bool DoDebugPrint { get; } = false;

        public static void DebugPrint(string msg)
        {
            if (DoDebugPrint)
                Console.WriteLine(msg);
        }
    }
}
