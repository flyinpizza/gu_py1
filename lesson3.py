# #1
# def div_two():
#
#     try:
#         dividend = float(input("Enter the dividend: "))
#         divider = float(input("Enter the divider: "))
#         division = dividend / divider
#     except ZeroDivisionError:
#         print("You can't divide by 0, silly")
#     except:
#         print("Something went wrong. Try entering numbers.")
#     else:
#         return (division)
#
# print(div_two())

# #2
#
# def contact_info(**kwargs):
#     contact_card = [
#         f"{i} = {j}"
#         for i, j in kwargs.items()
#     ]
#     return f" ".join(contact_card)

# #3
#
# def my_func (a, b, c):
#     my_list = [a, b, c]
#     my_list.sort()
#     sum_two_max = my_list[1] + my_list[2]
#     return sum_two_max

# #4
#
# def my_func(base, power):
#     if power == 0:
#         return 1
#     else:
#         return (1/base) * my_func(base, (power+1))

# #5
#
# def sum_num_from_string(fstring_of_numbers):
#     flist_of_numbers = fstring_of_numbers.split(" ")
#     flist_of_floats = []
#     for i in flist_of_numbers:
#         i = float(i)
#         flist_of_floats.append(i)
#     fsum_of_floats = sum(flist_of_floats)
#     return fsum_of_floats
#
# string_of_numbers = input("Enter numbers separated by space. Type '!!' to finish: ")
# previous_sum = 0
# if string_of_numbers.endswith('!!') == False:
#     sum_of_numbers = sum_num_from_string((string_of_numbers)) + previous_sum
#     print(f"Sum of numbers os {sum_of_numbers}")
#     string_of_numbers = input("Enter numbers separated by space. Type '!!' to finish: ")
#     previous_sum = sum_of_numbers
# elif string_of_numbers != '!!':
#     string_of_numbers_replace = string_of_numbers.replace('!!','')
#     sum_of_numbers = sum_num_from_string(string_of_numbers_replace)
#     print(f"Sum of numbers os {sum_of_numbers}. Process is finished.")
# else:
#     print("Process is finished.")


