
# fruits     = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats      = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[0][0])  # returns the first index & first element 

# To iterate through the list of lists...
# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

#--------------------------------#

# Let's create a 9-digit cell-phone keypad
'''
We'll use a tuple since we need our numbers to be:
-> ordered
-> changeable
-> and tuples are simply faster, so we should use them when possible
'''

num_pad = ((1,2,3), 
           (4,5,6), 
           (7,8,9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

'''
Visualizing Execution
First Iteration (row = (1,2,3))
    Inner loop:
    print(1, end=" ") → Output: `1 `
    print(2, end=" ") → Output: `1 2 `
    print(3, end=" ") → Output: `1 2 3 `
print() moves to a new line.

Second Iteration (row = (4,5,6))
Inner loop:
    print(4, end=" ") → Output: `4 `
    print(5, end=" ") → Output: `4 5 `
    print(6, end=" ") → Output: `4 5 6 `
print() moves to a new line.

Third Iteration (row = (7,8,9))
Inner loop:
    print(7, end=" ") → Output: `7 `
    print(8, end=" ") → Output: `7 8 `
    print(9, end=" ") → Output: `7 8 9 `
print() moves to a new line.

Fourth Iteration (row = ("*",0,"#"))
Inner loop:
    print("*", end=" ") → Output: `* `
    print(0, end=" ") → Output: `* 0 `
    print("#", end=" ") → Output: `* 0 # `
print() moves to a new line.

Final Output
1 2 3
4 5 6
7 8 9
* 0 #
Each row prints on its own line, forming a numeric keypad layout.
'''

print("Hello World!")