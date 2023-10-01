from . import cli
from . import converter


def main():
    args = cli.parse_arguments()
    converter.convert(
        input_image=args.input,
        output=args.output or args.input.with_suffix(".ico"),
        icon_sizes=[(x, x) for x in args.sizes]
    )


if __name__ == "__main__":
    main()
