numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

greater_than_10 = list(filter(lambda x: x > 10, squared))
print("Greater than 10:", greater_than_10)