import argparse
from contextlib import suppress


def required_list() -> argparse.ArgumentParser:
    # positional with no default.
    parser = argparse.ArgumentParser()
    parser.add_argument("mylist", nargs="+")
    return parser


def optional_list() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mylist", action="append")
    return parser


def list_with_default_none() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("mylist", nargs="*")
    return parser


print(required_list().parse_args("1 2 3".split()))
with suppress(SystemExit):
    print(required_list().parse_args([]))

# print(list_with_default_none().parse_args([]))

print(optional_list().parse_args([]))
# print(optional_list().parse_args(["--mylist", "1", "2"]))
print(optional_list().parse_args(["--mylist", "1", "--mylist", "2"]))
