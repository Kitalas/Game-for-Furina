# list1 = [1,2,3,4,5,6,7,8,9]
# #
# # print(type(lis1))
# #
# # list_iter_obj = iter(lis1)
# # print(type(list_iter_obj))
#
# list2 = []
# for i in list1:
#     list2.append(i**2)
# print(list2)

# def generator(num1, num2):
#     if num1 < num2:
#         step = 1
#     else:
#         step = -1
#         count = num1 - num2
#     value = num2
#     for i in range(count):
#         yield value
#         value += step
#
# for i in generator(20,10):
#     print(i)

import random

def random_generator(count):
    for i in range(count):
        yield random.randint(1, 100)

count_of_numbers = 1000
random_numbers = [number * 2 for number in random_generator(count_of_numbers)]
