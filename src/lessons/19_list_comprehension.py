# List comprehension = A concisew ay to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

#------------------------------#

# This is a lot to write...
# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
# print(doubles)


# Let's use a list comprehension to make it compact and easy to read
# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)


# Let's triple this time..
# triple = [y * 3 for y in range(1, 11)]
# print(triple)


# Let's square each number this time..
# squares = [z * z for z in range(1, 11)]
# print(squares)


# Let's create a list of fruits and upper-case them
# fruits = ["apple", "banana", "coconut", "watermelon"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)


# Create a list of the first character per element
# fruits = ["apple", "banana", "coconut", "watermelon"]
# fruits = [fruit[0] for fruit in fruits]
# print(fruits)

#------------------------------#

# Now let's work with conditions!

# Create a list of positive numbers
# numbers = [1, -1, 2, -2, 3, -3, 4, -4]
# positive_nums = [num for num in numbers if num >= 0]
# print(positive_nums)


# Create a list of even numbers
# Create a list of odd numbers
# numbers = [1, -1, 2, -2, 3, -3, 4, -4]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(odd_nums)


# Create a list of passing grades (60 or above)
# Create a list of failing grades (less than 60)
grades = [80, 90, 100, 55, 43, 1, 0, -30, 60, 61]
passing_grades = [grade for grade in grades if grade >= 60]
failing_grades = [grade for grade in grades if grade < 60]
print(f"Passing Grades: {passing_grades}")
print(f"Failing Grades: {failing_grades}")