cities_input = input("Enter city names separated by comma: ")
cities = [city.strip() for city in cities_input.split(',')]

print("Total cities:", len(cities))

k_cities = 0
for city in cities:
    if city.lower().startswith('k'):
        k_cities += 1
print("Cities starting with 'K':", k_cities)

cities.sort()
print("Cities in alphabetical order:", cities)