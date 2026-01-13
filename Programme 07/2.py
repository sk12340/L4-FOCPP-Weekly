def letters_in_any(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_one_only(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))

print(letters_in_any("hello", "world"))
print(letters_in_both("hello", "world"))
print(letters_in_one_only("hello", "world"))