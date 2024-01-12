from pyfiglet import Figlet

def print_with_design(text):
    design = Figlet (font = 'standard')
    print("\033[95m" + "=" * 40)
    print("\033[95m" + design.renderText(text))
    print("\033[95m" + "=" * 40)


def find_the_biggest_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
    
num1 = float(input("Enter the First Number: "))
num2 = float(input("Enter the Second Number: "))
num3 = float(input("Enter the Third Number: "))

biggest_number = find_the_biggest_number(num1, num2, num3)

print_with_design("The biggest number is:")
print(f"\033[96m{biggest_number}")
    