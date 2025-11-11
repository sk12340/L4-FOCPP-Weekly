def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Converts Fahrenheit to Celsius."""
    return (f - 32) * 5/9

# Test both functions
print("20°C is", celsius_to_fahrenheit(20), "°F")
print("68°F is", fahrenheit_to_celsius(68), "°C")