from . import cli
from . import converter


def main():
    args = cli.parse_arguments()
    converter.convert(args.input, args.output)


if __name__ == "__main__":
    main()
