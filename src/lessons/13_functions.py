# function = A block of reusable code
#            place () after the function name to invoke it

# return = statement used to end a function
#          and send a result back to the caller

#-------------------------#

# Creating a happy birthday function
# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# happy_birthday("Bro", 10)
# happy_birthday("Steve", 20)
# happy_birthday("Joe", 30)

#-------------------------#

# Creating an invoice function
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Joe", 100.01, "01/02")

#-------------------------#

# Creating functions to add/subtract/multiply/divide two numbers
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

#-------------------------#

# Creating a function to print a user's first and last name
# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = create_name("brian", "nguyen")
# print(full_name)