filename = input("Enter file name: ")
count = 0

with open(filename, 'r') as f:
    for line in f:
        if line.strip():
            if line.strip()[0].lower() in 'aeiou':
                count += 1

print(f"Lines starting with vowel: {count}")