def remove_last_character(s):
    """Returns the string with the last character removed. If 1 or fewer chars, returns original."""
    if len(s) <= 1:
        return s
    return s[:-1]

# Test the function
test_string = input("Enter a string: ")
result = remove_last_character(test_string)
print("Result:", result)