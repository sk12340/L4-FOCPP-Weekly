infile = input("Enter file name: ")
outfile = "reversed.txt"

with open(infile, 'r') as f:
    lines = f.readlines()

with open(outfile, 'w') as f:
    for line in lines:
        f.write(line.strip()[::-1] + "\n")

print("Reversed lines written to reversed.txt")