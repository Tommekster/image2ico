from .cli_arguments import CliArguments

__all__ = ["CliArguments", "parse_arguments"]


def parse_arguments() -> CliArguments:
    args = CliArguments().parse_args()
    return args
