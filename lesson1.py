# #1
# country = input("Enter the name of the country you live in: ")
# city = input("Enter the name of the city you live in: ")
# street = input("Enter the name of the street you live on: ")
# home_number = int(input("Enter the number of the building you live in: "))
# postal = input("Enter your postal code: ")
#
# print(f"Your address is {home_number} {street}, {city}, {country}, {postal}")

# #2
# seconds_input = int(input("Enter time period in seconds: "))
# hours = seconds_input // 3600
# minutes = (seconds_input % 3600) // 60
# seconds = seconds_input % 60
# print(f"{hours:02}:{minutes:02}:{seconds:02}")

# #3
# num_n = int(input("Enter a number from 0 to 9: "))
# num_nn = int(str(num_n) + str(num_n))
# num_nnn = int(str(num_n) + str(num_nn))
# sum_all = num_n + num_nn + num_nnn
# print(f"{num_n}+{num_nn}+{num_nnn}={sum_all}")

# #4
# number = input("Enter an integer ")
# number_int = int(number)
# b = 0
# digits = len(number)
# while digits >= 1:
#     x = number_int % 10
#     digits -= 1
#     number_int = number_int // 10
#     if x > b:
#         b = x
# print(b)

# #5
# revenue = float(input("Input the revenue: "))
# cost = float(input("Input the costs: "))
# profit = revenue - cost
# profitabilty = profit / revenue
# if profit > 0:
#     print("You are operating at a profit")
#     staff = int(input("What's the number of employees: "))
#     profit_per_emp = profit / staff
#     print(f"Profitability is {profitabilty:.2}. Profit per employee is {profit_per_emp:.2}")
# elif profit < 0:
#     print("You are operating at a loss")
# else:
#     print("You are operating at zero profit")


# #6
#
# start = float(input("Enter the length of the run in day one, kilometers: "))
# goal = float(input("Enter the goal length of the run, kilometers: "))
# days = 1
# route = start
# while route < goal:
#     route = route * (1.1)
#     days += 1
# print(days)



