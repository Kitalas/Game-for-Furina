import math

def menu():
    print("Виберіть операцію:")
    print("1. Додати")
    print("2. Відняти")
    print("3. Помножити")
    print("4. Розділити")
    print("5. Квадратний корінь")
    print("6. Вийти")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    return "Ділення на нуль!"

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    return "Неможливо взяти квадратний корінь з від'ємного числа!"

while True:
    menu()
    choice = input("Введіть ваш вибір: ")

    if choice == '6':
        break

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if choice == '1':
            print("Результат:", add(num1, num2))
        elif choice == '2':
            print("Результат:", subtract(num1, num2))
        elif choice == '3':
            print("Результат:", multiply(num1, num2))
        elif choice == '4':
            print("Результат:", divide(num1, num2))

    elif choice == '5':
        num = float(input("Введіть число: "))
        print("Результат:", square_root(num))
    else:
        print("Неправильний вибір. Спробуйте ще раз.")

