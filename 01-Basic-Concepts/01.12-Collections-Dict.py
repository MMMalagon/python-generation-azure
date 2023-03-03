empty_dict = {}
fruits = {"OR": "orange", "LE": "lemon",
          "GR": "grapefruit", "LI": "lime", "TA": "tangerine"}

# print dict
print(fruits)

# print value given a key (throws exception if does not exist)
print(fruits["OR"])

# print value given a key (returns none if does not exist)
print(fruits.get("OR"))
print(fruits.get("WA"))

# print dict length
print(len(fruits))

# replace value from a given key
fruits["OR"] = "watermelon"
fruits.update({"OR": "grape"})
print(fruits["OR"])

# add new key-value pair
fruits["ME"] = "melon"
print(fruits["ME"])

# delete key and its value given a key
fruits.pop("OR")
del fruits["LI"]

# iterate keys
for key in fruits:
    print(f"Key: {key} - Value: {fruits[key]}")

# iterate keys (alternative)
for key in fruits.keys():
    print(f"Key: {key} - Value: {fruits[key]}")

# iterate values
for value in fruits.values():
    print(f"Value: {value}")

# iterate keys-values
for key, value in fruits.items():
    print(f"Key: {key} - Value: {value}")

print(fruits)
