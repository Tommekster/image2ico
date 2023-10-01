from pathlib import Path
from typing import Literal
from tap import Tap


class CliArguments(Tap):
    input: Path
    output: Path = Path("output.ico")
    sizes: list[Literal[16, 24, 32, 48, 64, 128, 255]] = [
        16, 24, 32, 48, 64, 128, 255
    ]

    def configure(self) -> None:
        self.add_argument("input")
        self.add_argument("-o", "--output")
        self.add_argument(
            "-s", "--sizes", help="list of icon sizes (ex: --sizes 16 32)")
