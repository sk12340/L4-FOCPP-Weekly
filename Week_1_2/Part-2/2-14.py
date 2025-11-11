text = input("Enter a string: ")

digits = 0
letters = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print(f"Letters: {letters}")
print(f"Digits: {digits}")