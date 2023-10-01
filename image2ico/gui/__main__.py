from .app import App
from .cli_arguments import CliArguments


def main():
    args = CliArguments().parse_args()
    root = App(args.input)
    root.mainloop()


if __name__ == "__main__":
    main()
