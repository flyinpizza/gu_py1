# #1
#
# file_output = open("output.txt", "w", encoding="utf-8")
# string_to_write = "1"
# content = []
# while len(string_to_write) > 0:
#     string_to_write = input("Enter the string to be written in the file: ")
#     content.append(string_to_write + "\n")
# content.pop()
# file_output.writelines(content)
# file_output.close()

# #2
#
# with open("output.txt") as fobj:
#     counter = 0
#     words_in_line = []
#     for line in fobj:
#         number_of_words = len(line.split(" "))
#         words_in_line.append(number_of_words)
#         counter +=1
#     print(counter, words_in_line)

# #3
#
# with open("salaries.txt") as fobj:
#     employees = []
#     employee = {}
#     employees_below_twenty = []
#     salaries = 0
#     employee_number = 0
#     for line in fobj:
#         line_list = line.split(" ")
#         name = line_list[0]
#         salary = line_list[1].replace("\n","")
#         employee.update({name : salary})
#         employees.append(employee)
#         if float(salary) < 20000:
#             employees_below_twenty.append(name)
#         salaries = salaries + float(salary)
#         employee_number += 1
#     average_salary = salaries/employee_number
# print(f"Last names of employees that make less than 20000 per month are {employees_below_twenty}.\nAverage salary in the firm is {average_salary:.2f}.")

# #5
#
# import functools
# try:
#     with open("number_file.txt", "w", encoding="utf-8") as fobj:
#         content = input("Enter numbers devided by spaces: ")
#         fobj.write(content)
#         fobj.seek(0)
#         list_of_numbers = content.split(" ")
#         sum_of_numbers = functools.reduce(lambda a,b: float(a)+float(b), list_of_numbers)
#     print(sum_of_numbers)
# except ValueError:
#     print("Make sure you input only numbers.")
# except IOError:
#     print("Input-output error.")

# #6
# def sep_numbers(x):
#     x_num = ""
#     for i in x:
#         if i.isdigit() == True:
#             x_num = x_num + i
#     return x_num
#
# with open("text_6.txt", "r", encoding="utf-8") as subject_file:
#     subject_hours_dict = {}
#     for line in subject_file:
#         line_list = line.split( )
#         line_list_numbers = []
#         for i in line_list:
#             i_numbers = sep_numbers(i)
#             if len(i_numbers) > 0:
#                 line_list_numbers.append(int(i_numbers))
#         hours = sum(line_list_numbers)
#         subject = line_list[0].replace(":", "")
#         subject_hours_dict[subject] = hours
#     print(subject_hours_dict)

#7
import json
with open("text_7.txt", "r", encoding="utf-8") as f_firms:
    profits = []
    firms_and_profits = []
    for line in f_firms:
        firm_dict = {}
        firm_list = line.split(" ")
        firm_name = firm_list[0]
        profit = int(firm_list[2]) - int(firm_list[3])
        profits.append(profit)
        firm_dict[firm_name] = profit
        firms_and_profits.append(firm_dict)
    av_profit = sum(profits)/len(profits)
    firms_and_profits.append({"Average profit" : av_profit})
    print(firms_and_profits)
with open("text_7.json", "w", encoding="utf-8") as f_firms_profits:
    json.dump(firms_and_profits, f_firms_profits,)