from . import cli
from . import converter


def main():
    args = cli.parse_arguments()
    converter.convert(args.input.as_posix(), args.output.as_posix())


if __name__ == "__main__":
    main()
