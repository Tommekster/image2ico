import sys
from pathlib import Path
import tkinter as tk


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

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=10, pady=5, sticky="wens")

    tk.Label(frame, text="Input Image").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(frame).grid(row=0, column=1, sticky="we", padx=5, pady=5)
    tk.Button(
        frame, text="Select file..."
    ).grid(row=0, column=2, sticky="we", padx=5, pady=5)

    tk.Label(frame, text="Output Icon").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(frame).grid(row=1, column=1, sticky="we", padx=5, pady=5)
    tk.Button(
        frame, text="Select location..."
    ).grid(row=1, column=2, sticky="we", padx=5, pady=5)

    tk.Label(frame, text="Sizes").grid(row=2, column=0, padx=5, pady=5)
    sizes_frame = tk.Frame(frame)
    sizes_frame.grid(row=2, column=1, padx=5, pady=5)
    tk.Checkbutton(sizes_frame, text="16").pack(side="left")
    tk.Checkbutton(sizes_frame, text="24").pack(side="left")
    tk.Checkbutton(sizes_frame, text="32").pack(side="left")
    tk.Checkbutton(sizes_frame, text="48").pack(side="left")
    tk.Checkbutton(sizes_frame, text="64").pack(side="left")
    tk.Checkbutton(sizes_frame, text="128").pack(side="left")
    tk.Checkbutton(sizes_frame, text="255").pack(side="left")

    tk.Button(
        frame,
        text="Convert",
        bg="#2176C1",
        fg="white",
        font=("Font", 24)
    ).grid(
        row=3, column=0, columnspan=3,
        sticky="we", padx=5, pady=5, ipady=5
    )

    root.mainloop()


if __name__ == "__main__":
    main()
