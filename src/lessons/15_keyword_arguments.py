# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional   2. default   3. KEYWORD   4. arbitrary

#------------------------------#
# Examples of using keyword arguments

# Example 1
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "Spongebob", "Squarepants")                  # without keyword arguments
# hello("Hello", title="Mr.", first="Spongebob", last="Squarepants") # with keyword arguments
# hello("Hello", last="Squarepants", first="Spongebob", title="Mr.") # keyword arguments in different orders
# hello(last="Squarepants", "Hello", first="Spongebob", title="Mr.") # this is wrong: "Hello" is a positional argument, so it must precede keyword args


# Example 2
# for x in range(1, 11):
#     print(x, end=" ")     # end is a keyword argument that we used in previous lessons


# Example 3
# print("1", "2", "3", "4", "5", sep="-")   # sep is another keyword argument

#------------------------------#
# Exercise

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)