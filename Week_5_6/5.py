filename = input("Enter file name: ")
with open(filename, 'r') as f:
    words = f.read().lower().split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

most_word = max(word_count, key=word_count.get)
print(f"Most frequent word: '{most_word}' ({word_count[most_word]} times)")