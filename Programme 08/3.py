import sys

if len(sys.argv) != 3:
    print("Usage: python grep.py <pattern> <file>")
    sys.exit(1)

pattern = sys.argv[1]
filename = sys.argv[2]

with open(filename) as f:
    for line in f:
        if pattern in line:
            print(line.rstrip())