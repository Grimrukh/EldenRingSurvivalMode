using System;

namespace PropertyHook
{
    /// <summary>
    /// A dynamic pointer starting from an array of bytes scanned for in the target process.
    /// </summary>
    public abstract class PHPointerAOB : PHPointer
    {
        /// <summary>
        /// The AOB to scan for.
        /// </summary>
        public byte?[] AOB { get; set; }

        /// <summary>
        /// The result of the AOB scan.
        /// </summary>
        public IntPtr AOBResult;

        /// <summary>
        /// Creates a new AOB pointer.
        /// </summary>
        public PHPointerAOB(PHook parent, byte?[] aob, int[] offsets) : base(parent, offsets)
        {
            AOB = aob;
        }

        /// <summary>
        /// Returns the result of the AOB scan.
        /// </summary>
        public override IntPtr ResolveSpecific()
        {
            return AOBResult;
        }

        /// <summary>
        /// Scan for the AOB and store the adddress in `AOBResult`.
        /// Returns `true` if the scan succeeded and `false` otherwise.
        /// Called automatically by `PHook` for registered `PHPointerAOB`s.
        /// </summary>
        public abstract bool ScanAOB(AOBScanner scanner);

        internal void DumpAOB()
        {
            AOBResult = IntPtr.Zero;
        }
    }
}
