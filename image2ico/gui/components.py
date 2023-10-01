from typing import cast
import tkinter as tk
from .commands import Commands
from .variables import Variables


class Components(Commands, Variables):
    def __setup_components__(self):
        frame = tk.Frame(cast(tk.Tk, self))
        frame.grid(row=0, column=0, padx=10, pady=5, sticky="wens")

        tk.Label(frame, text="Input Image").grid(
            row=0, column=0, padx=5, pady=5)
        tk.Entry(
            frame,
            textvariable=self.input_file
        ).grid(row=0, column=1, sticky="we", padx=5, pady=5)
        tk.Button(
            frame,
            text="Select file...",
            command=self.open_file
        ).grid(row=0, column=2, sticky="we", padx=5, pady=5)

        tk.Label(frame, text="Output Icon").grid(
            row=1, column=0, padx=5, pady=5)
        tk.Entry(
            frame,
            textvariable=self.output_file
        ).grid(row=1, column=1, sticky="we", padx=5, pady=5)
        tk.Button(
            frame,
            text="Select location...",
            command=self.save_file
        ).grid(row=1, column=2, sticky="we", padx=5, pady=5)

        tk.Label(frame, text="Sizes").grid(row=2, column=0, padx=5, pady=5)
        sizes_frame = tk.Frame(frame)
        sizes_frame.grid(row=2, column=1, padx=5, pady=5)
        for size, variable in self.sizes.items():
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
            command=self.convert
        ).grid(
            row=3, column=0, columnspan=3,
            sticky="we", padx=5, pady=5, ipady=5
        )
