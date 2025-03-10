# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to left-most position
# :  = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 12000.34

# Formatting as decimal precision
# print(f"Price 1 is ${price1:.1f}") # :.1f places a decimal, carries 1 space, and f meaning float
# print(f"Price 2 is ${price2:.2f}")
# print(f"Price 3 is ${price3:.3f}") 

# Adding spaces within the value
# print(f"Price 1 is ${price1:10}") # each value now has a total of 10 spaces
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}") 

# Preceding a number with zero padding
# print(f"Price 1 is ${price1:010}") # each value now has a total of 10 spaces
# print(f"Price 2 is ${price2:010}") # and is zero padded
# print(f"Price 3 is ${price3:010}") 

# Left/Right/Center justifying values
# print(f"Price 1 is ${price1:<10}") # left justify
# print(f"Price 2 is ${price2:>10}") # right justify
# print(f"Price 3 is ${price3:^10}") # center align 

# Displaying positive values (if any)
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}") 
# print(f"Price 3 is ${price3:+}")  

# Adding a thousands comma separator
# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}") 

# Mix n Matching practice
# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")