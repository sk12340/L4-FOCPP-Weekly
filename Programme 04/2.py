def count_case(string):
    """Returns the count of uppercase and lowercase letters in a string."""
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

# Test the function
test_string = input("Enter a string to analyze: ")
uppers, lowers = count_case(test_string)
print("Uppercase letters:", uppers)
print("Lowercase letters:", lowers)