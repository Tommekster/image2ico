import sys
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from image2ico import converter
from .folder_opener import FolderOpener


def main():
    root = tk.Tk()
    root.title("Image2ico")
    root.resizable(False, False)

    icon_file = Path(
        sys.executable
        if getattr(sys, "frozen", False)
        else __file__+"/../.."
    ).resolve().parent.joinpath("image2ico.png").as_posix()
    icon = tk.PhotoImage(file=icon_file)
    root.iconphoto(True, icon)

    input_file = tk.StringVar()
    output_file = tk.StringVar()
    sizes: dict[int, tk.IntVar] = {
        size: tk.IntVar(value=True)
        for size in [16, 24, 32, 48, 64, 128, 255]
    }

    def open_file():
        filename = filedialog.askopenfilename(
            title="Select image",
            filetypes=(
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.ico"),
                ("All files", "*.*"),
            )
        )
        filepath = Path(filename)
        input_file.set(str(filepath))
        output_file.set(str(filepath.with_suffix(".ico")))

    def save_file():
        filename = filedialog.asksaveasfilename(
            title="Save as",
            filetypes=(
                ("Icon files", "*.ico"),
                ("All files", "*.*"),
            ),
            initialfile=output_file.get()
        )
        output_file.set(filename)

    def convert():
        input_image=Path(input_file.get())
        output=Path(output_file.get())
        converter.convert(
            input_image=input_image,
            output=output,
            icon_sizes=[(x, x) for x, v in sizes.items() if v.get()]
        )
        FolderOpener().open(output)
        root.destroy()

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=5, sticky="wens")

    tk.Label(frame, text="Input Image").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(
        frame,
        textvariable=input_file
    ).grid(row=0, column=1, sticky="we", padx=5, pady=5)
    tk.Button(
        frame,
        text="Select file...",
        command=open_file
    ).grid(row=0, column=2, sticky="we", padx=5, pady=5)

    tk.Label(frame, text="Output Icon").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(
        frame,
        textvariable=output_file
    ).grid(row=1, column=1, sticky="we", padx=5, pady=5)
    tk.Button(
        frame,
        text="Select location...",
        command=save_file
    ).grid(row=1, column=2, sticky="we", padx=5, pady=5)

    tk.Label(frame, text="Sizes").grid(row=2, column=0, padx=5, pady=5)
    sizes_frame = tk.Frame(frame)
    sizes_frame.grid(row=2, column=1, padx=5, pady=5)
    for size, variable in sizes.items():
        tk.Checkbutton(
            sizes_frame,
            text=size,
            variable=variable
        ).pack(side="left")

    tk.Button(
        frame,
        text="Convert",
        bg="#2176C1",
        fg="white",
        font=("Font", 24),
        command=convert
    ).grid(
        row=3, column=0, columnspan=3,
        sticky="we", padx=5, pady=5, ipady=5
    )

    root.mainloop()


if __name__ == "__main__":
    main()
