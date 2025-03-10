# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("India"))   # output: New Delhi


# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")


# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# How to iterate over each key and print all keys
# keys = capitals.keys()
# for key in keys:
#     print(key)

# How to iterate over each value and print all values
# values = capitals.values()
# for value in values:
#     print(value)

# How to iterate over each key & value and print them all
# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")
