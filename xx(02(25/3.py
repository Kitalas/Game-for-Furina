# class MyIterator:
#     def __init__(self, numbers:int):
#         self.numbers = numbers
#     def __iter__(self):
#         self. current = 0
#         return self
#     def __next__(self):
#         if self.current >= self.numbers:
#             raise StopIteration
#
#         self.current += 1
#         return self.current
#
# obj = MyIterator(10)
# a = iter(obj)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))


# class MyIterator:
#     def __init__(self, start_numbers:int, end_num:int):
#         self.end_num = end_num
#         self.start_numbers = start_numbers
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start_numbers >= end_num:
#             raise self
#         result = self.start_numbers
#         self.start_numbers += 1
#
# for i in MyIterator(20, 10)
#     print(1)


def infinite_iterator():
    num = 0
    while True:
        yield num
        num += 1

for number in infinite_iterator():
    print(number)
    if number >= 10:  # Зупинка після 10 для запобігання нескінченного виводу
        break