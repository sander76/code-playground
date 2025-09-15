import argparse

parser = argparse.ArgumentParser(exit_on_error=False)

parser.add_argument("--integers", type=int)

try:
    parser.parse_args("--integers a".split())
except argparse.ArgumentError:
    print("caught error")
