'''
for loops = execute a block of code a fixed number of times.
            You can iterate over a range, string, sequence, etc.
'''

# Example 1) For loop to count from 1 to 10
# for x in range(1, 11):
#     print(x)

# Example 2) For loop to count backwards from 10 to 1
# for x in reversed(range(1, 11)):
#     print(x)
# print("HAPPY NEW YEAR!")

# Example 3) For loop to iterate through a credit card number
# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#     print(x)

# Example 4) For loop to iterate, but skip an element
# for x in range(1, 21):
#     if x == 13:
#         continue        # Continue is a flow control tool used in loops to alter the normal execution sequence.
#     print(x)            # In this case, we're using continue to skip 13 as the program iterates.

# Example 5) For loop to iterate, but stop at a given element
for x in range(1, 21):
    if x == 13:
        break            # Break is another flow control tool used in loops to alter the execution sequence.
    else:                # In this case, we're using break to stop before the iteration reaches 13
        print(x)