from colorama import Back, Style

def calculate_total_amount(orange, apple):
    orange_price = 25
    apple_price = 20 
    total_amount = (orange * orange_price) + (apple * apple_price)
    return total_amount

apple = int(input("How many apples you want to buy?"))
orange = int(input("How many orange you want to buy?"))

total = calculate_total_amount(orange, apple)

print(f"The Total amount you need to pay is {total} Pesos")




