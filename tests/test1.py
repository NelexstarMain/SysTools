import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--word", type=str, help="searched word", required=True)

args = parser.parse_args()

print(args.word)
