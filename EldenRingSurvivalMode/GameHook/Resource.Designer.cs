﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace EldenRingSurvivalMode.GameHook {
    using System;
    
    
    /// <summary>
    ///   A strongly-typed resource class, for looking up localized strings, etc.
    /// </summary>
    // This class was auto-generated by the StronglyTypedResourceBuilder
    // class via a tool like ResGen or Visual Studio.
    // To add or remove a member, edit your .ResX file then rerun ResGen
    // with the /str option, or rebuild your VS project.
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("System.Resources.Tools.StronglyTypedResourceBuilder", "17.0.0.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    public class Resource {
        
        private static global::System.Resources.ResourceManager resourceMan;
        
        private static global::System.Globalization.CultureInfo resourceCulture;
        
        [global::System.Diagnostics.CodeAnalysis.SuppressMessageAttribute("Microsoft.Performance", "CA1811:AvoidUncalledPrivateCode")]
        internal Resource() {
        }
        
        /// <summary>
        ///   Returns the cached ResourceManager instance used by this class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        public static global::System.Resources.ResourceManager ResourceManager {
            get {
                if (object.ReferenceEquals(resourceMan, null)) {
                    global::System.Resources.ResourceManager temp = new global::System.Resources.ResourceManager("EldenRingSurvivalMode.GameHook.Resource", typeof(Resource).Assembly);
                    resourceMan = temp;
                }
                return resourceMan;
            }
        }
        
        /// <summary>
        ///   Overrides the current thread's CurrentUICulture property for all
        ///   resource lookups using this strongly typed resource class.
        /// </summary>
        [global::System.ComponentModel.EditorBrowsableAttribute(global::System.ComponentModel.EditorBrowsableState.Advanced)]
        public static global::System.Globalization.CultureInfo Culture {
            get {
                return resourceCulture;
            }
            set {
                resourceCulture = value;
            }
        }
        
        /// <summary>
        ///   Looks up a localized string similar to 0:  0f 29 89 90 00 00 00    movaps XMMWORD PTR [rcx+0x90],xmm1
        ///7:  41 50                   push   r8
        ///9:  49 b8 fe fe fe fe fe    movabs r8,0xfefefefefefefefe
        ///10: fe fe fe
        ///13: f3 41 0f 10 08          movss  xmm1,DWORD PTR [r8]
        ///18: f3 0f 11 49 1c          movss  DWORD PTR [rcx+0x1c],xmm1
        ///1d: 49 b8 fe fe fe fe fe    movabs r8,0xfefefefefefefefe
        ///24: fe fe fe
        ///27: f3 41 0f 10 08          movss  xmm1,DWORD PTR [r8]
        ///2c: f3 0f 11 49 60          movss  DWORD PTR [rcx+0x60],xmm1
        ///31: 49 b8 fe fe fe fe fe    m [rest of string was truncated]&quot;;.
        /// </summary>
        public static string EldenRingFog {
            get {
                return ResourceManager.GetString("EldenRingFog", resourceCulture);
            }
        }
    }
}
