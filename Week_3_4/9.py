def update_sales(sales, day, amount):
    if day in sales:
        sales[day] += amount
    else:
        sales[day] = amount
    return sales

weekly_sales = {'Mon': 100, 'Tue': 150}
day = input("Enter day: ")
amount = int(input("Enter amount: "))
updated = update_sales(weekly_sales, day, amount)
print("Updated sales:", updated)