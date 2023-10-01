from typing import cast
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox
from image2ico import converter
from .folder_opener import FolderOpener
from .variables import Variables

class Commands(Variables):
    def open_file(self):
        filename = filedialog.askopenfilename(
            title="Select image",
            filetypes=(
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico"),
                ("All files", "*.*"),
            )
        )
        self.__set_input_image__(Path(filename))

    def save_file(self):
        filename = filedialog.asksaveasfilename(
            title="Save as",
            filetypes=(
                ("Icon files", "*.ico"),
                ("All files", "*.*"),
            ),
            initialfile=self.output_file.get()
        )
        self.output_file.set(filename)

    def convert(self):
        input_image=Path(self.input_file.get())
        if not input_image.is_file():
            messagebox.showerror(
                title="Missing input image",
                message="Input image is not file!"
            )
            return

        output=Path(self.output_file.get())
        output.parent.mkdir(parents=True, exist_ok=True)

        try:
            converter.convert(
                input_image=input_image,
                output=output,
                icon_sizes=[(x, x) for x, v in self.sizes.items() if v.get()]
            )
        except Exception as e:
            messagebox.showerror(
                title="Converting error",
                message=str(e)
            )
            return

        FolderOpener().open(output)
        cast(tk.Tk,self).destroy()

    def __set_input_image__(self, filepath:Path):
        self.input_file.set(str(filepath))
        self.output_file.set(str(filepath.with_suffix(".ico")))