import sys

if len(sys.argv) != 2:
    print("Usage: python nl.py <filename>")
    sys.exit(1)

with open(sys.argv[1], 'r') as f:
    for i, line in enumerate(f, 1):
        print(f"{i:4}  {line.rstrip()}")