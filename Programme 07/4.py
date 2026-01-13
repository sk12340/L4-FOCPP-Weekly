def top_six_letters(text):
    text = text.lower()
    freq = {}
    for ch in text:
        if ch.isalpha():
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
    # Sorting by frequency
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:6]

message = "Hello world, welcome to Python programming!"
print(top_six_letters(message))