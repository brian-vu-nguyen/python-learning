'''
while loop = execute some code WHILE some condition remains TRUE

Make sure you program a way to escape the while loop
or else there will be an infinite loop
'''

#---------------------------------------------------#

''' Example of why while loops are useful '''

# The below code would not continuously prompt you to enter your name
# name = input("Enter your name: ")

# if name == "":
#     print("You did not enter your name")
# else:
#     print(f"Hello {name}")

#---------------------------------------------------#

# Let's try a while loop instead
# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ") # escape out of while loop
# print(f"Hello {name}")

'''
Executing the above code would continuously prompt the user to enter something
then it will stop
'''

#---------------------------------------------------#

# Let's try asking for the user's age
# age = int(input("Enter your age: "))

# while age == "":
#     print("You did not enter your age")
#     age = int(input("Enter your age: ")) # escape out of while loop 
# print(f"You are {age} years old.") 

#---------------------------------------------------#

'''
We can also allow the user to manually end the while loop by introducing logical operators.
'''

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")

#---------------------------------------------------#

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")