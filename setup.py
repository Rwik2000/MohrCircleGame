import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["matplotlib",
                                  'pygame',
                                  'numpy',
                                  'sympy',
                                  'time',
                                  'random',
                                  ],
                     "include_files" : ["Images/iitgn.png",
                                        "Fonts/pt mono bold.ttf",
                                        "Fonts/pt mono regular.ttf"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Mohr's Circle",
        version = "0.1",
        description = "final project",
        options = {"build_exe": build_exe_options},
        executables = [Executable("mohr_game.py", base=base),
                       Executable("MohrCircle_new.py"),
                       Executable("utilities/mohr_fonts.py"),
                       Executable("utilities/mohr_screen.py"),
                       Executable("utilities/mohr_user_input.py"),
                       Executable("window_types/mohr_general.py"),
                       Executable("window_types/mohr_quiz.py"),
                    #    Executable("utilities"),
                    #    Executable("window_types"),
                    #    Executable("Images/iitgn.png"),
                    #    Executable("Fonts/pt mono bold.ttf"),
                    #    Executable("Fonts/pt mono regular.ttf")
                       ])