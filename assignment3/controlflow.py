def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent/100)
        return discounted_price
    else:
        return price
    
price = float(input("Enter thr original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

if final_price != price:
    print("Final price after applying the discount: $", round(final_price))
else:
    print("No discount applied. The total price is: $", round(price))