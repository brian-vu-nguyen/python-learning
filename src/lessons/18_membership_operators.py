# Membership operators = used to test whether a value or variable is found in a sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in

#-----------------------------#

# Example: Checking a string
# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")

#-----------------------------#

# Example: Checking a dictionary
# grades = {"Sandy":"A", 
#           "Squidward":"B", 
#           "Spongebob":"C", 
#           "Patrick":"D"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

#-----------------------------#

# Checking if characters exist in a string
# email = "abc@gmail.com"

# if "@" in email and "." in email:
#     print(f"{email} is valid")
# else:
#     print(f"{email} is invalid")