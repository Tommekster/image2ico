from pathlib import Path
from tap import Tap

class CliArguments(Tap):
    input: Path|None = None
    
    def configure(self) -> None:
        self.prog="image2ico"
        self.description="Image to icon converting tool"
        self.add_argument(
            "input", help="input image file", nargs="?")