# using [] to create lists
empty_list = []
fruits = ["orange", "lemon", "grapefruit", "lime", "tangerine"]

# printing list content
print(fruits)

# printing an item of the list (3 - lime)
print(fruits[3])

# printing length or number of items on the list
print(len(fruits))

# printing number of times an item appears on the list
print(fruits.count("watermelon"))  # does not exist
print(fruits.count("lime"))  # does exist and only one

# modifing item content on a list given an index (replacing idx 3 lime with watermelon)
fruits[3] = "watermelon"
print(fruits)
print(fruits[3])

# adding new items using append function
fruits.append("apple")
fruits.append("kiwi")

# adding new item given a positon or index using insert function
fruits.insert(1, "passionfruit")  # is this a drake reference???!!!

# adding item if it does not exist on the list
if ("banana" not in fruits):
    fruits.append("banana")

# removing item given an index using pop function (6 - apple)
fruits.pop(6)

# removing item given the item value using remove function
fruits.remove("orange")

# removing item if does exist
if ("watermelon" in fruits):
    fruits.remove("watermelon")

# reversing list items by using reverse function
fruits.reverse()

# ordering list items by using sort function
fruits.sort()
fruits.sort(reverse=True)

# copying every list item
empty_list = fruits.copy()

# deleting every single item value on the list
fruits.clear()
