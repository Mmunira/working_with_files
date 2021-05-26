



### 'try', 'except' and 'finally' block of codes
# They as if and else block -

# create a function called greetings
# def greetings():
# pass

# name = "devops"
# year = 2021
# print(name + year)

# ##Second Iteration
# def open_using_with_and_print(file):
#     try:
#         with open("order.txt", "r") as file:
#             for line in file.readline():
#                 print(line.rstrip('\n'))
# # try code block ends
#     except FileNotFoundError as errmsg:
#         print("sorry file not found ;) ")
#
#     finally:
#         return "Thank you for visiting hope to see you again!"
#
# print(open_using_with_and_print("order.txt"))

# create a function called open_with_to_write_to_file  write/add/append
# display the data with the add items - item names - pizza, cake, avocado, biryani, pasta

def open_with_to_write_to_file(file):
    try:
        with open("order.txt", 'a') as file:
            file.write("\nPizza\nCake\nAvocado\nBiriyani\nPasta")
    except FileNotFoundError as errmsg:
        print("Sorry file not found")

    finally:
        print("Thank you for visiting hope to see you again!")

open_with_to_write_to_file('order.txt')