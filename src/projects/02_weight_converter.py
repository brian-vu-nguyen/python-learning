# Python weight converter
# 1 kilogram = 2.20462 pounds

weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    result = weight * 2.20462
    units = "lbs."
    print(f"Weight conversion: {round(result, 2)} {units}")
elif unit == "L":
    result = weight / 2.20462
    units = "kgs."
    print(f"Weight conversion: {round(result, 2)} {units}")
else:
    print(f"{unit} is not a valid unit.")