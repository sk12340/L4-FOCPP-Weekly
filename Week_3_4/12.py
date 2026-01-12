def common_letters(word1, word2):
    common = []
    for letter in word1:
        if letter in word2 and letter not in common:
            common.append(letter)
    common.sort()
    return common

w1 = input("Enter first word: ")
w2 = input("Enter second word: ")
print("Common letters:", common_letters(w1, w2))