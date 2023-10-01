import sys
import tomli
from cx_Freeze import setup, Executable

icon = "image2ico.ico"

with open("pyproject.toml", "rb") as f:
    project = tomli.load(f)

bdist_msi_options = {
    "data": {
        "ProgId": [
            ("Prog.Id", None, None,
             "Image2ico: Image to icon converting tool", "IconId", None),
        ],
        "Icon": [
            ("IconId", icon),
        ],
        "Registry": [
            (
                "open-in-image2ico",
                -1,
                rf"Software\Classes\SystemFileAssociations\image\shell\open.image2ico_gui.exe",
                "",
                "Open in Image2Ico",
                "_cx_executable1__Executable_script_gui.py_"),
            (
                "open-in-image2ico-command",
                -1,
                rf"Software\Classes\SystemFileAssociations\image\shell\open.image2ico_gui.exe\command",
                "",
                "\"[TARGETDIR]image2ico_gui.exe\" \"%1\"",
                "_cx_executable1__Executable_script_gui.py_"),
        ]
    },
    "install_icon": icon,
    "upgrade_code": "{e23bcc11-1311-4630-adb2-2bb63c0ba45d}",
    "add_to_path": True,
    "directories": [
        ("ProgramMenuFolder", "TARGETDIR", "."),
        ("MyProgramMenu", "ProgramMenuFolder", "Image2ico"),
    ]
}


setup(
    name=project["tool"]["poetry"]["name"],
    version=project["tool"]["poetry"]["version"],
    description=project["tool"]["poetry"]["description"],
    author=project["tool"]["poetry"]["authors"][0],
    options={
        "build_exe": project["tool"]["distutils"]["build_exe"],
        "bdist_msi": bdist_msi_options,
    },
    executables=[
        Executable(
            'cli.py',
            icon=icon,
            target_name='image2ico',
        ),
        Executable(
            'gui.py',
            icon=icon,
            base='Win32GUI' if sys.platform == 'win32' else None,
            target_name='image2ico_gui',
            shortcut_name="Image2ico",
            shortcut_dir="MyProgramMenu",
        )
    ]
)
