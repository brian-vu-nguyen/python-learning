# Temperature Converter

# C -> F Formula: (°C × 9/5) + 32 = °F
# F -> C Formula: (°F − 32) × 5/9 = °C

unit = input("Is this temperature in Celcius or Fahrenheit? (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    result = round((temperature * (9/5) + 32), 1)
    print(f"The temperature is {result} °F")
elif unit == "F":
    result = round((temperature - 32) * (5/9), 1)
    print(f"The temperature is {result} °C")
else:
    print(f"{unit} is not a valid unit.")