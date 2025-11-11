def is_valid(number):
    """Returns True if number is between 0 and 100 (inclusive), else False."""
    return 0 <= number <= 100

# Test the function
test_value = int(input("Enter a number to test: "))
print(is_valid(test_value))