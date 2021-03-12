import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["common", "logs", "client", "unit_tests"],
}
setup(
    name="radif_messenger_client",
    version="0.3.3",
    description="radif_messenger_client",
    options={
        "build_exe": build_exe_options
    },
    executables=[Executable('client.py',
                            # base='Win32GUI',
                            targetName='server.exe',
                            )]
)
