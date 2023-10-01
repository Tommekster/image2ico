from . import cli
from . import converter


def main():
    args = cli.parse_arguments()
    converter.convert(args.input, args.output, [(x, x) for x in args.sizes])


if __name__ == "__main__":
    main()
