from cx_Freeze import setup, Executable

setup(
    name="hello",
    version="0.1",
    description="hello",
    executables=[Executable("jeux.py")]
    )