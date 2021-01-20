# #1
#
# my_list = [False, 1, "two", 2.33, [3, 4, "five"]]
# for i in my_list:
#     print(type(i))

# #2
# number_of_elements = int(input("How many elements are there in your list? "))
# my_list = []
# for i in range(number_of_elements):
#     list_element = input("Enter the next element: ")
#     my_list.append(list_element)
# number_of_pairs = number_of_elements // 2
# print(my_list)
# for i in range(number_of_pairs):
#     element = my_list[(i)*2]
#     my_list.pop((i)*2)
#     my_list.insert((i)*2+1,element)
# print(my_list)

# #3.list
#
# seasons = ["w", "w", "sp", "sp", "sp", "su", "su", "su", "a", "a", "a", "w"]
# season_names = {"w":"winter", "sp":"spring", "su":"summer", "a":"autumn"}
# month_number = int(input("Enter the number of the month, 1 to 12 "))
# index_number = month_number - 1
# season = season_names[seasons[index_number]]
# endings = {1:"st", 2:"nd", 3:"rd"}
# if index_number in range(3):
#     ending = endings[month_number]
# else:
#     ending = "th"
# print(f"The {month_number}{ending} month of the year is the {season} month.")

# #3.dict
#
# seasons_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer", 9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
# month_number = int(input("Enter the number of the month, 1 to 12 "))
# endings = {1:"st", 2:"nd", 3:"rd"}
# if month_number in range(4):
#     ending = endings[month_number]
# else:
#     ending = "th"
# season = seasons_dict[month_number]
# print(f"The {month_number}{ending} month of the year is the {season.lower()} month.")

# #4
#
# user_string = input("Enter your text ")
# text_list = user_string.split(" ")
# line_number = 1
# for i in text_list:
#     i_printable = i[:10]
#     print(f"{line_number}. {i_printable}")
#     line_number += 1

# #5
#
# initial_rating = [9, 5, 3, 2, 2]
# new_rating_element = int(input("Enter a new rating element: "))
# counter = 0
# for i in initial_rating:
#     if i >= new_rating_element:
#         counter += 1
# initial_rating.insert(counter, new_rating_element)
# print(initial_rating)

# #6
#
# number_of_item_names = int(input("How many item names are there in your list? "))
# items_list = []
# names_list = []
# prices_list = []
# quantities_list = []
# measurements_list = []
# item_number = 1
# for i in range(number_of_item_names):
#     item_name = input("What is the name of your item? ")
#     item_price = float(input("What is the price of your item? "))
#     item_quantity = float(input("What is the quantity of this item? "))
#     item_quantity_measure = input("What is the measure of quantity for this item? ")
#     item_dict = dict(name=item_name, price=item_price, quantity=item_quantity, measure=item_quantity_measure)
#     item_tuple = (item_number, item_dict)
#     items_list.append(item_tuple)
#     names_list.append(item_name)
#     prices_list.append(item_price)
#     quantities_list.append(item_quantity)
#     measurements_list.append(item_quantity_measure)
#     item_number += 1
# analytics = dict(names=names_list, prices=prices_list, quantities=quantities_list, measurements=measurements_list)
# print(analytics)
