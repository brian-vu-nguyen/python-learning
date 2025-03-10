# Python compound interest calculator

'''
Compound Interest Formula
A = P(1 + (r/n))^t

A = final amount
P = initial principle balance
r = interest rate
t = number of time periods elapsed
'''

principle = 0
rate = 0
time = 0

while True:                                                 # Loop starts
    principle = int(input("Enter the principle amount: "))  # Ask for input
    if principle < 0:                                       # Check if input is valid
        print("Principle can't be less than zero")          #    -> if principle < 0, print message and repeat loop
    else:                                                   # Once break is triggered, program continues to the next part
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} years: ${total:.2f}")