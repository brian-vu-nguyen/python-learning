# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in on your own)
#          useful to break up a large program reusable separate files
# print(help("modules"))


# Importing the math module
# import math as m   # we can alias the module and refer to its alias
# print(m.pi)


# Another way to import is using 'from'
# from math import 


# We can create our own modules
# See the module we created, '', to print the following... 
import example

result = example.pi
result = example.square(3)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)