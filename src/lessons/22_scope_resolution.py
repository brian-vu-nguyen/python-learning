# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# 1) Example of Local scope
# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()



# 2) Example of Enclosed scope 
#    i.e. accessing a variable within a nested function
# def func1():
#     x = 1

#     def func2():
#         x = 2  # uncomment this to see difference
#         print(x)
#     func2()

# func1()



# 3) Example of Global scope
# x = 3
# def func1():
#     print(x)

# def func2():
#     print(x)

# func1()
# func2()


# 4) Example of Built-in scope
from math import e  # Built-in version of 'e'
def func1():
    print(e)
e = 3               # Global version of 'e'... Uncomment to see difference
func1()