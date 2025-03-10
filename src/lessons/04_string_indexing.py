# indexing = accessing elements of a sequence using [] (aka: indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# Get the first element in the sequence
# print(credit_number[0])

# Get the first four elements
# print(credit_number[0:4])

# Get the 5th through 9th elements
# print(credit_number[5:9])

# Get all elements at 5th element and beyond
# print(credit_number[5:])

#----------------------------#

# Using negative numbers to retrieve elements in a reverse order

# Get the last element
# print(credit_number[-1])

# Get the second-to-last element
# print(credit_number[-2])

#----------------------------#

# Using the step argument

# Get every 2nd element in the list
# print(credit_number[::2])

#----------------------------#
      ### Exercise ###

# Get the last four digits of a credit card number
# last_four_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_four_digits}")

# Reverse the elements in the sequence
# reversed_credit_number = credit_number[::-1]
# print(reversed_credit_number)