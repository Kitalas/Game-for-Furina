# import time
#
#
# def red_lingh_decorator(func):
#     def wrapper():
#         print(colorama.Fore.RED)
#         func()
#         print(colorama.Fore.RESET)
#     return wrapper
#
#
# def green_lingh_decorator(func):
#     def wrapper(*args, *kwargs):
#         start_time = time.time()
#         result = func(*args, *kwargs)
#         end_time = time.time()
#         print(f"Час исполнение игры: {end_time - start_time} сек")
#     return wrapper
#
#     @timer_decorator
#     def example_function(n):
#         total = 0
#         for i in range(n):
#             total += i
#         return total
#
#
# result = example_function(10653284)
# print(result)