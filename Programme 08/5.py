import sys
import re

def load_dictionary():
    return {"hello", "world", "python", "program", "test", "file", "text"}

if len(sys.argv) != 2:
    print("Usage: python spell.py <filename>")
    sys.exit(1)

dictionary = load_dictionary()
with open(sys.argv[1]) as f:
    text = f.read()
    # Extracting words
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    misspelled = [w for w in words if w not in dictionary]

print("Misspelled words:", set(misspelled))
