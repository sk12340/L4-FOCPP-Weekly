filename = input("Enter file name: ")
vowels = consonants = digits = special = 0

with open(filename, 'r') as f:
    text = f.read()
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if char.lower() in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        else:
            special += 1

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Digits: {digits}")
print(f"Special: {special}")