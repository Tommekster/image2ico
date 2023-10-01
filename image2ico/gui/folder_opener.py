import sys
from pathlib import Path, WindowsPath
from subprocess import run


class FolderOpener:
    def open(self, path: Path | str):
        path = Path(path) if isinstance(path, str) else path
        assert isinstance(path, Path)

        if path.exists():
            if sys.platform == "win32":
                windows_path = WindowsPath(path)
                if path.is_file():
                    run(["explorer", "/select,", windows_path])
                else:
                    run(["explorer", windows_path])
            elif sys.platform == "darwin":
                if path.is_file():
                    run(["open", "-R", path])
                else:
                    run(["open", path])
            elif sys.platform == "linux":
                if path.is_file():
                    run(["xdg-open", path.parent])
                else:
                    run(["xdg-open", path])
