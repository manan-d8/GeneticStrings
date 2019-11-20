import cx_Freeze

executables = [cx_Freeze.Executable("Genetic Search visual.py")]

cx_Freeze.setup(
    name="A bit Racey",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["C:/Users/Personal/Documents/python projects/Genetic algo/hpunk.ttf",
                                            "C:/Users/Personal/Documents/python projects/Genetic algo/oreos.ttf",
                                            "C:/Users/Personal/Documents/python projects/Genetic algo/East_Lift.ttf"]}},
    executables = executables

    )