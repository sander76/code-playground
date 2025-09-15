from argparse import ArgumentParser

parser = ArgumentParser(exit_on_error=False)
parser.add_argument("value1")
parser.add_argument("value2")
parser.add_argument("--val3", default="abc")

if __name__ == "__main__":
    args = parser.parse_args()

    print(args.value1)
    print(args.value2)
    print(args.val3)
