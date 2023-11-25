import math 

def calculate_max_apple(money, apple_price):

    max_apple = money // apple_price
    remaining_money = money % apple_price
    return max_apple, remaining_money

money = float(input("Enter the amount of money you have: "))
apple_price = float(input("Enter the price of an apple: "))

max_apple, remaining_money = calculate_max_apple(money, apple_price)

print(f"With {money} you have, you can buy a {max_apple} apples ")
print(f" You will have {remaining_money} pesos remaining")
