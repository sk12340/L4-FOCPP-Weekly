filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, 'r') as f:
    lines = f.readlines()

print(f"'{word}' found in lines:")
for i, line in enumerate(lines, 1):
    if word in line:
        print(i)