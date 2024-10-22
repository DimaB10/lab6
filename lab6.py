def arithmetic_operations(a, b):
    print(f"Сума: {a} + {b} = {a + b}")
    print(f"Різниця: {a} - {b} = {a - b}")
    print(f"Добуток: {a} * {b} = {a * b}")
    if b != 0:
        print(f"Частка: {a} / {b} = {a / b}")
    else:
        print("Ділення на нуль неможливе")

def main():
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))
    arithmetic_operations(num1, num2)

main()
import math
def sum_of_roots(num):
    sqrt_root = math.sqrt(num)  
    cube_root = num ** (1/3)   
    return sqrt_root + cube_root

def main():
    num = float(input("Введіть додатне число: "))
    
    if num >= 0:
        result = sum_of_roots(num)
        print(f"Сума квадратного і кубічного коренів числа {num}: {result}")
    else:
        print("Число повинно бути додатним")

main()
