infile = input("Enter input file: ")
outfile = input("Enter output file: ")

with open(infile, 'r') as f:
    words = f.read().split()

unique_words = []
for word in words:
    if word not in unique_words:
        unique_words.append(word)

unique_words.sort()

with open(outfile, 'w') as f:
    for word in unique_words:
        f.write(word + "\n")

print("Unique words written.")