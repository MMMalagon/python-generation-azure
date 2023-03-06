import json

citrus_fruits = ["orange", "lemon", "grapefruit", "lime", "tangerine"]

citrus_fruits_json = json.dumps(citrus_fruits)

print(citrus_fruits)
print(citrus_fruits[2])  # grapefruit
print(type(citrus_fruits))  # list

print(citrus_fruits_json)  # unicode
print(citrus_fruits_json[2])  # o
print(type(citrus_fruits_json))  # str


citrus_fruits_2 = json.loads(citrus_fruits_json)

print(citrus_fruits_2)
print(citrus_fruits_2[2])  # grapefruit
print(type(citrus_fruits_2))  # list
