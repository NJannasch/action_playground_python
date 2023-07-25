import argparse

parser = argparse.ArgumentParser(description="Print a message.")
parser.add_argument("--message", type=str, help="The message to print.")

args = parser.parse_args()

print(args.message)
