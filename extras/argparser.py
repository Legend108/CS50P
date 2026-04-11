import argparse

parser = argparse.ArgumentParser()
# --help shows the help part and adds a menu to
# -s number gets returned from args.s and we can add as much as we want
parser.add_argument("-s", type=int, help="Repeat hello", default=1)
args = parser.parse_args()
for _ in range(args.s):
    print("Hello")