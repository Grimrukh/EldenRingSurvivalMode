
                                  E L D E N   R I N G 
   _____ _    _ _______      _________      __     _        __  __  ____  _____  ______ 
  / ____| |  | |  __ \ \    / /_   _\ \    / /\   | |      |  \/  |/ __ \|  __ \|  ____|
 | (___ | |  | | |__) \ \  / /  | |  \ \  / /  \  | |      | \  / | |  | | |  | | |__   
  \___ \| |  | |  _  / \ \/ /   | |   \ \/ / /\ \ | |      | |\/| | |  | | |  | |  __|  
  ____) | |__| | | \ \  \  /   _| |_   \  / ____ \| |____  | |  | | |__| | |__| | |____ 
 |_____/ \____/|_|  \_\  \/   |_____|   \/_/    \_\______| |_|  |_|\____/|_____/|______|

                                         v1.0
                                    
                                     by Grimrukh
                       
              with special thanks to @JanZielasko, @Thens_DeS, @king_bore_haha

=== INSTRUCTIONS ===

0) Meditate for five minutes upon the importance of disabling anticheat for
   Elden Ring. Decide if you will do it using Mod Engine 2 (see below) or
   through some other means.

1) Install the static modded game files from one or more `Game (X)` subdirectories
   in the mod folder. The combination of subdirectories you install will determine
   which features of the mod are activated, as detailed below.

       Game (DARKNESS ONLY)
           If you ONLY want the night darkness effects of the mod, install these
           files only. Ignore the SHARED and OPTIONS folders entirely. You will
           still need to run the executable while playing the game to see the
           darkness effects (see step 2 below).

       Game (SHARED)
           If you want MORE than just darkness, always install these files. They
           include icons and text used by all the features in OPTIONS.

       Game (OPTIONS)
           Navigate the very high-tech subfolders inside this folder to determine
           which set of additional mod files to install. Each feature can be
           'ENABLED' or 'DISABLED' depending on your choice in each subfolder.

           The feature sets are:

               Survival -- hunger, thirst, temperature, and Torrent nerf.
               Weapon Tree -- new weapon crafting/upgrading system.
               Diseases -- random diseases with hidden cure recipes.

           Install the files you find after your 'Diseases' choice. If you
           forget to install any of these OPTIONS subdirectories, you will get
           darkness only.

           Note that if you want all three of these OPTIONS enabled but do NOT
           want darkness, follow the same installation instructions, but skip
           step 2 below (that is, just don't run the Darkness executable).

   You have two methods for installing all of the above files:
    
    a) Download Mod Engine 2 for Elden Ring, copy the mod files into Mod 
       Engine's `mod` folder, and run it with `launchmod_eldenring.bat`. 
       This is the easiest way to play and requires no UXM or backups:
       
            https://github.com/soulsmods/ModEngine2/releases
    
    b) Unpack your Elden Ring installation with UXM, make back ups of
       the original files, and copy-paste the mod files directory into 
       your installation `Game` folder, replacing all existing files. 
       You will have to restore the original files yourself to uninstall 
       later, and disable anticheat yourself when playing. 
       
            [You can find UXM on the FromSoft modding Discord server.]

2) Run `SurvivalModeDarkness.exe`. This is a simple companion program that 
   will connect to your Elden Ring game and create the darkness effects. If
   you don't want the darkness effects, you can simply skip this step. If
   you close the program accidentally, you can restart it without needing
   to restart or even quit out of your Elden Ring game. Note that darkness
   effects will ONLY work if you run this executable AND are using one of
   the two modded events from `Game (Full Mod)` or `Game (Darkness Only)`.

3) Run Elden Ring, either through `launchmod_eldenring.bat` if using Mod
   Engine 2 (which disables anticheat) or through Steam if using UXM
   (after disabling anticheat yourself).

=== SUPPORT ===

Thank you for playing!

This mod was created as part of my annual tradition of making an off-the-wall
mod for LobosJr's St Jude charity drive in May. It's also the first mod I've
made for a game other than the original Dark Souls.

If you like my mods, and want to support my ongoing activities (including
Dark Souls: Nightfall), you can become a supporter on Patreon!

    https://patreon.com/Grimrukh

Any support is greatly appreciated <3
  
=== CREDITS ===

Mod assistance:

    JZ (@JanZielasko) for helping with the darkness effects
    Thens (@Thens_DeS) for weapon recipes and new icons
    George (@king_bore_haha) for weapon recipes and new item text

I used my own software Soulstruct, which currently has limited 
support for Elden Ring EMEVD files when installed with Python.
You can find tutorials for Soulstruct (with Dark Souls) on my
YouTube channel.
    
    https://github.com/grimrukh/soulstruct
    https://www.youtube.com/c/Grimrukh

Other legends creating FromSoft modding tools used by this mod:

    TKGP (SoulsFormats, PropertyHook, Yapped)
    vawser (Yapped for Elden Ring)
    katalash (Mod Engine 2)
    HotPocketRemix (EMEVD tools)
    thefifthmatt (EMEVD/ESD tools)
