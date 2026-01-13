def unique_sorted_letters(s):
    letters = []
    for ch in s.lower():
        if ch.isalpha() and ch not in letters:
            letters.append(ch)
    letters.sort()
    return letters

print(unique_sorted_letters("cheese"))