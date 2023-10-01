from pathlib import Path
from typing import Literal
from tap import Tap


class CliArguments(Tap):
    input: Path
    output: Path | None = None
    sizes: list[Literal[16, 24, 32, 48, 64, 128, 255]] = [
        16, 24, 32, 48, 64, 128, 255
    ]

    def configure(self) -> None:
        self.add_argument(
            "input", help="input image file")
        self.add_argument(
            "-o", "--output", help="output ICO filename (default: input_file.ico)")
        self.add_argument(
            "-s", "--sizes", help="list of icon sizes (ex: --sizes 16 32)")
