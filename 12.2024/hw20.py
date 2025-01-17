#exp 1
list_num = []
print(min(list_num))
print(max(list_num))
print(sum(list_num))
print(sum(list_num) / len(list_num))

#exp2
list_1 = list(map(int, input('Введите элементы первого списка через пробел: ').split()))

list_2 = list(map(int, input('Введите элементы второго списка через пробел: ').split()))

result_list = list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))

print('\n' + '-'*50 + '\n')
print('Итоговый список (в прям. посл.):', result_list)
print('\n' + '-'*50 + '\n')
print('Итог. спис. (в обр. посл.):', result_list[::-1])
print('\n' + '-'*50 + '\n')


result_list.sort()

print('Cорт. (Возрастание):', result_list)
result_list.sort(reverse=True)
print('Cорт. (Убывание):', result_list)

#exp3
start = int(input("Введите начало промежутка: "))
end = int(input("Введите конец промежутка: "))

simple_numbers = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
else:
    simple_numbers.append(num)

print("Простые числа:", simple_numbers)
choice = input("Хотите увидеть сумму/произведение? (1 - сумма/2 - произведение): ")

if choice == '1':
    summa = 0
    for number in simple_numbers:
        summa += number
        print("Cуммa:", summa)
elif choice == '2':
    product = 1
for number in simple_numbers:
    product *= number
    print("Произведение:", product)

#exp4
print("Example of a list: [4, 11, 3, 8, 6]")
list_of_ints = [int(x) for x in input("Enter elements of your list:").split()]
while True:
   print("Menu: \nPress 1 to display list in reverse order \nPress 2 to display list in ascending order \nPress any other key to exit")
   choice = input("Please enter your choice:")
   if choice == '1':
       list_of_ints.reverse()
       print("List in reverse order:")
       print(list_of_ints)
   elif choice == '2':
       list_of_ints.sort()
       print("List in ascending order:")
       print(list_of_ints)
   else:
       break

#exp5
int_list = [2, 4, 145, 8, 10, 52, 14]
new_list = []

for i in int_list:
    if i % 2 != 0:
        new_list.append(i)
        repeat = int(input('Введите количество повторов списка: '))
    for _ in range(repeat):
        new_list += new_list
        int_list.clear()

#exp6
user_input = int(input('Введите число: '))
if user_input in new_list:
    print(f'Число {user_input} повторяется {new_list.count(user_input)} раз и находится на {new_list.index(user_input) + 1} позиции.')
else:
    print('Такого числа нет в списке.')