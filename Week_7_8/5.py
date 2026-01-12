import converter

km = float(input("Enter km: "))
print(f"{km} km = {converter.km_to_miles(km):.2f} miles")

c = float(input("Enter Celsius: "))
print(f"{c}°C = {converter.celsius_to_fahrenheit(c):.2f}°F")