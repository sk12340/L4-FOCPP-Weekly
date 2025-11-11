codes = [80, 121, 116, 104, 111, 110]
characters = []
print("   Codes to characters:")
for code in codes:
    char = chr(code)
    characters.append(char)
    print(f"   {code} → '{char}'")
result_string = ''.join(characters)
print(f"   Combined word: '{result_string}'")

print("\n" + "=" * 50)
print("END OF PART 1")
print("=" * 50)