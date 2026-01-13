print("Beckett Pizza Plaza 4-for-3 Offer")
print("==================================\n")

prices = []

pizza_number = 1
while pizza_number <=4:
    try:
        price = float(input(f"Enter price of pizza #{pizza_number}: "))

        if price <=0:
            print("Please enter a valid price!")
        else:
            prices.append(price)
            pizza_number +=1

    except ValueError:
        print("Please enter a correct value")  

Total_before_discount = sum(prices)
cheapest_pizza = min(prices)

final_amt = Total_before_discount - cheapest_pizza
discount_percentage = (cheapest_pizza/Total_before_discount)*100

print(f"\nOrder Total is Npr{final_amt:.2f}, and the discount % is {discount_percentage:.2f}%!")