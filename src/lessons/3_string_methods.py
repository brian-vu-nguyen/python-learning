# name = input("Enter your full name: ")

# 1) len() function will give length of a string
# name = input("Enter your full name: ")
# result = len(name)
# print(result)

# Bonus: any() takes an iterable (like a list, tuple, or generator) 
#              and returns True if at least one element is True.
#   Why any() is Powerful
#       ✅ Short-circuits (stops early when True is found).
#       ✅ More efficient than looping manually.
#       ✅ Works with different iterables (lists, tuples, generators, etc.).

# 2) .find() method will find the first occurrence of a given character
# then will provide the position
# name = input("Enter your full name: ")
# result = name.find(" ")
# print(result)

# 3) .rfind() method will find the last occurrence of a given character
#    then will provide the position
# name = input("Enter your full name: ")
# result = name.rfind("N")
# print(result)

# 4) .capitalize() method will capitalize the first letter of the string
# name = input("Enter your full name: ")
# result = name.capitalize()
# print(result)

# 5) .upper() method will capitalize all letters of the string
# 6) .lower() method will lowercase all letters of the string
# 7) .title() method will capitalize the first letter of all words in a string
# 8) .isdigit() method will return boolean if string contains only digits
# 9) .isalpha() method returns boolean if string contains only alphabetical characters
# 10) .count() method counts # of given character
# 11) .replace() method replaces a given character with a new one  <-- very useful method!
# phone_number = input("Enter your phone number: ")
# result = phone_number.replace("-", "")
# print(result) 




# Practice: Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username cannot be longer than 12 characters.")
elif " " in username: 
    print("Username can't contain spaces")
elif any(char.isdigit() for char in username):
    print("Username can't contain numbers")
else:
    print(f"Welcome {username}") 