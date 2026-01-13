countries = {}

while True:
    country = input("Enter country (or 'quit' to exit): ").strip().lower()
    if country == 'quit':
        break
    if country in countries:
        print(f"Capital: {countries[country]}")
    else:
        capital = input(f"Capital for {country}: ").strip()
        countries[country] = capital
        print("Saved.")