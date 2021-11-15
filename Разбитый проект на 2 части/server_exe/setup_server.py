import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "server", "unit_tests"],
}
setup(
    name="radif_messenger_server",
    version="0.3.3",
    description="radif_messenger_server",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('server.py',
                            # Чтобы убрать консоль, разкоментировать строку:
                            # base='Win32GUI',
                            targetName='server.exe',
                            )]
)
