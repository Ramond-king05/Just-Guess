import cx_Freeze

executables = [cx_Freeze.Executable("guess.py")]

cx_Freeze.setup(
    name="Ramond Guess Game",
    options={"build_exe": {"packages":["pygame"],
                           }},
    executables = executables

    )