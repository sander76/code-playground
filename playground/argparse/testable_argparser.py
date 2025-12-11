from argparse import ArgumentParser
from typing import Sequence


def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("value")
    return parser


def parse_args(args: Sequence[str] | None = None):
    parser = create_parser()
    parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args()
