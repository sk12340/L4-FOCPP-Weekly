import sys

if len(sys.argv) != 3:
    print("Usage: python diff.py <file1> <file2>")
    sys.exit(1)

with open(sys.argv[1]) as f1, open(sys.argv[2]) as f2:
    if f1.read() == f2.read():
        print("Files are identical.")
    else:
        print("Files are different.")