import sys
from pathlib import Path
import tkinter as tk
from .components import Components
from .variables import Variables


class App(tk.Tk, Components, Variables):
    def __init__(self, input_image: Path | None, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.__setup_variables__()
        self.__setup_components__()
        self.__setup_icon__()
        if input_image:
            self.__set_input_image__(input_image.resolve())

        self.title("Image2ico")
        self.resizable(False, False)

    def __setup_icon__(self):
        icon_file = Path(
            sys.executable
            if getattr(sys, "frozen", False)
            else __file__+"/../.."
        ).resolve().parent.joinpath("image2ico.png").as_posix()
        icon = tk.PhotoImage(file=icon_file)
        self.iconphoto(True, icon)
