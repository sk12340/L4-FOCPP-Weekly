import sys

if len(sys.argv) != 2:
    print("Usage: python wc.py <filename>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    chars = sum(len(line) for line in lines)
    print(f"Lines: {len(lines)}")
    print(f"Characters: {chars}")