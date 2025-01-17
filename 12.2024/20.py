#-----------------------
a = 10
print(id(a))
a = a + 5
print(id(a))
#-----------------------
numbers = (10,20,30)
numbers = numbers + (10,20,30)
#-----------------------
a = 5
b = 5
c = 5
print(id(a))
print(id(b))
print(id(c))
#------------------------
numbers_list = [10,20,30,40]
print(len(numbers_list))
print(numbers_list[0])
print(numbers_list[-1])
print(numbers_list[1:3])
print(numbers_list.count(10))
print(numbers_list.index(20))
for number in numbers_list:
    print(number)
#-----------------------
numbers_list = [10,20,30,40]
numbers_list.append('hello')
print(numbers_list)
#----------------------
# student = []
#
# while True:
#     a = int(input("1, 2 or 0: "))
#     if a == 1:
#         student.append(input("name: "))
#         print(student)
#     if a == 2:
#         for name in student:
#             print(name)
#     if a == 0:
#         break
#----------------------
numbers = [10,20,30,40]
numbers2 = [99,98,97]
numbers.append(50)
numbers.insert(0,100)
numbers.insert(3,100)
numbers.extend(numbers2)

numbers[0] = 99
numbers.remove(99)
numbers.pop(1)
remove_number = number.pop(1)
del numbers[-1]
print(numbers)

numbers1 = [10,20,7,5,2,4,30]

# numbers1.reverse()
# print(numbers1)

reversed_numbers = list(reversed(numbers1))
print(numbers1)
print(reversed_numbers)
numbers1.sort()

sorted_numbers = sorted(numbers1)
print(numbers1)
print(sorted_numbers)
