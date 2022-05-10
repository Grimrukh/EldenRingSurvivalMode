using System;

namespace PropertyHook
{
    /// <summary>
    /// A dynamic pointer starting from the base address of an array of bytes scanned for in the target process.
    /// </summary>
    public class PHPointerAOBAbsolute : PHPointerAOB
    {
        /// <summary>
        /// Creates a new absolute AOB pointer.
        /// </summary>
        public PHPointerAOBAbsolute(PHook parent, byte?[] aob, params int[] offsets) : base(parent, aob, offsets) { }

        /// <summary>
        /// Scan for the AOB and store the adddress in `AOBResult`.
        /// Returns `true` if the scan succeeded and `false` otherwise.
        /// Called automatically by `PHook` for registered `PHPointerAOB`s.
        /// </summary>
        public override bool ScanAOB(AOBScanner scanner)
        {
            AOBResult = scanner.Scan(AOB);
            return AOBResult != IntPtr.Zero;
        }
    }
}
