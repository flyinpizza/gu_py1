# #1
# from sys import argv
#
# script_name, hours_worked, pay_per_hour, bonus = argv
# try:
#     salary = float(hours_worked)*float(pay_per_hour)+float(bonus)
#     print(salary)
# except:
#     print("Parameters should be numbers: hours worked, pay per hour and bonus.")

# #2
# initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [initial_list[i] for i in range(1, len(initial_list)) if initial_list[i] > initial_list[i-1]]
# print(new_list)

# #3
# list_of_numbers = [el for el in range(20, 241) if el%21==0 or el%20==0]
# print(list_of_numbers)

# #4
# initial_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list = [initial_list[i] for i in range(len(initial_list)) if initial_list.count(initial_list[i])<2]
# print(new_list)

# #5
# import functools
# generated_list = [n for n in range(100, 1001, 2)]
# #print(generated_list)
# list_sum = functools.reduce(lambda a,b: a*b, generated_list)
# print(list_sum)

# #6a
# import itertools
# start = int(input("With what number should we begin the iteration? "))
# stop = int(input("What should be the last number of the iteration? "))
# for i in itertools.count(start):
#     if i > stop:
#         break
#     else:
#         print(i)

# #6b
# import itertools
# iter_list = [1, 'two', '3', [4, 5], {"6":7,"8":9}]
# list_repetitions = int(input("How many times should we print the list out?"))
# iter = itertools.cycle(iter_list)
# for i in range(list_repetitions):
#     for j in range(len(iter_list)):
#         print(next(iter))

# #7
# '''''''''
# попытка реализовать факториал через рекурсию
# def fact(n):
#     if n == 0:
#         factorial = 0
#     elif n == 1:
#         factorial = 1
#     else:
#         factorial = n * fact(n-1)
#     return factorial
#
# print(fact(5))
# '''''''''
#
# import functools
# def func(n):
#     if n == 0:
#         factorial = 0
#     else:
#         n_list = [el for el in range(1, n+1)]
#         factorial = functools.reduce(lambda a,b: a*b, n_list)
#     return factorial
#
# print(func(5))