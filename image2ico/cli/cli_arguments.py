from pathlib import Path
from tap import Tap


class CliArguments(Tap):
    input: Path
    output: Path = Path("output.ico")

    def configure(self) -> None:
        self.add_argument("input")
        self.add_argument("-o", "--output")
