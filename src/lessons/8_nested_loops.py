'''
nested loop = A loop within a loop (outer, inner)
              outer loop:
                  inner loop:

You can have the following:
    -> for loop inside for loop
    -> for loop inside while loop
    -> while loop inside for loop
    -> while loop inside while loop
'''
#----------------------------------------#

# Here's a for loop counting from 1 to 9
# for x in range(1, 10):
#     print(x, end="")

#----------------------------------------#

# Let's use a nested loop to repeat the above
# for x in range(3):           # Outer loop to repeat inner loop 3 times
#     for y in range(1, 10):   #      Inner loop to count from 1 to 9
#         print(y, end="")     #          printing iterations on a single line 
#     print()                  # prints each iteration on separate lines

#----------------------------------------#

# Exercise: Write a program to ask a user to input the rows, columns, and symbol
#           Then have the symbol fill in the area of the given rows & columns

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print() 