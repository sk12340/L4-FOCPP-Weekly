def count_characters(string):
    digits = 0
    letters = 0
    special = 0
    
    for char in string:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            letters += 1
        else:
            special += 1
    
    return digits, letters, special

text = input("Enter a string: ")
d, l, s = count_characters(text)
print(f"Digits: {d}")
print(f"Letters: {l}")
print(f"Special characters: {s}")