using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EldenRingSurvival
{
    /// <summary>
    /// My utility class for constructing a byte array for direct
    /// injection into process memory.
    /// </summary>
    internal class MemBuilder
    {
        readonly List<byte> mem = new();
        readonly Dictionary<string, (int, int)> reserved = new();

        public int Offset => mem.Count;

        static List<byte> ParseHexString(string hex)
        {
            List<byte> result = new();
            foreach (string b in hex.Split(' '))
                result.Add(byte.Parse(b, System.Globalization.NumberStyles.AllowHexSpecifier));
            return result;
        }

        public void Write(IEnumerable<byte> bytes)
        {
            mem.AddRange(bytes);
        }

        public void Write(string hex)
        {
            Write(ParseHexString(hex));
        }

        public void Write(byte b)
        {
            mem.Add(b);
        }

        public byte[] Finish()
        {
            if (reserved.Count > 0)
                throw new Exception("Cannot call `MemBuilder.Finish()` when reserved names remain.");
            return mem.ToArray();
        }

        public void Reserve(string name, int size)
        {
            if (reserved.ContainsKey(name))
                throw new Exception($"Name '{name}' is already reserved.");
            reserved[name] = (size, Offset);
            for (int i = 0; i < size; i++)
                Write(0xFE);  // placeholder bytes
        }

        public int GetReservedOffset(string name)
        {
            if (!reserved.ContainsKey(name))
                throw new Exception($"Cannot get offset of unreserved name '{name}'.");
            return reserved[name].Item2;
        }

        public void Fill(string name, IEnumerable<byte> value)
        {
            if (!reserved.ContainsKey(name))
                throw new Exception($"Cannot fill unreserved name '{name}'.");
            (int size, int offset) = reserved[name];
            byte[] valueArray = value.ToArray();
            if (valueArray.Length != size)
                throw new Exception($"Number of bytes to write to reserved '{name}' does not match reserved size: {size}");
            for (int i = 0; i < valueArray.Length; i++)
                mem[offset + i] = valueArray[i];
            reserved.Remove(name);
        }

        public void Fill(string name, string hex)
        {
            Fill(name, ParseHexString(hex));
        }
    }
}
