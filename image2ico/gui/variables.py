import tkinter as tk


class Variables:
    input_file: tk.StringVar
    output_file: tk.StringVar
    sizes: dict[int, tk.IntVar]

    def __setup_variables__(self):
        self.input_file = tk.StringVar()
        self.output_file = tk.StringVar()
        self.sizes = {
            size: tk.IntVar(value=True)
            for size in [16, 24, 32, 48, 64, 128, 255]
        }
