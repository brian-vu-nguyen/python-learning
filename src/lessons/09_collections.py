# collections = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#----------------------------------------------------#

### Lists ###
#   List  = [] ordered and changeable. Duplicates OK

# fruits = ["apple", "orange", "banana", "coconut"]

# Counting elements in a sequence
# print(len(fruits))

# Finding if an element exists
# print("pineapple" in fruits)

# Replacing an element
# fruits[0] = "pineapple"
# for fruit in fruits:
#     print(fruit)

# Appending an element at the end of a collection
# fruits.append("pineapple")
# print(fruits)

# Remove an element
# fruits.remove("apple")
# print(fruits)

# Inserting an element
# fruits.insert(0, "strawberry")
# print(fruits) 

# Sorting a collection in ascending order (alphabetically)
# fruits.sort()
# print(fruits)

# Sorting a collection in descending order (alphabetically)
# fruits.sort()
# fruits.reverse()
# print(fruits) 

# Ordering in reverse order
# fruits.reverse()
# print(fruits) 

# Clear a list
# fruits.clear()
# print(fruits)

# Counting element occurrences
# print(fruits.count("apple"))     # output: 1
# print(fruits.count("pineapple")) # output: 0

#----------------------------------------------------#

### Sets ###

#   Set   = {} unordered and immutable, but Add/Remove OK. NO Duplicates
# good when working with constants, like a set of colors

# fruits = {"apple", "orange", "banana", "coconut"}


# Sets are immutable, so the below code will not work
# fruits[0] = "pineapple"
# for fruit in fruits:
#     print(fruit)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

#----------------------------------------------------#

### Tuples ###

#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
# can only count and index tuples

# fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(fruits.count("coconut"))
# print(fruits.index("apple")) 

