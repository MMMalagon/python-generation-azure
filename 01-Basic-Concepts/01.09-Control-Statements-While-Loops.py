from time import sleep

value = 0

while (value < 5):
    # value += 1
    print(f"Data value is: {value}")
    sleep(1.0)
    value = value + 1

print("While loop ends")


citrus_fruits = ["orange", "lemon", "grapefruit", "lime", "tangerine"]

idx = 0

while (idx < len(citrus_fruits)):
    print(f"{idx}: {citrus_fruits[idx]}")
    idx += 1
else:
    print("OMG!")


idx = 0

while (idx < len(citrus_fruits)):
    idx += 1
    continue  # does invoke else statement
    print(f"{idx}: {citrus_fruits[idx]}")
    idx += 1
else:
    print("OMG!!")


idx = 0

while (idx < len(citrus_fruits)):
    print(f"{idx}: {citrus_fruits[idx]}")
    idx += 1
    break  # doesn't invoke else statement
else:
    print("OMG!!!")


idx = 20

while (idx < len(citrus_fruits)):  # because condition isn't meet, it jumps directly to else statement
    print(f"{idx}: {citrus_fruits[idx]}")
    idx += 1
    break  # doesn't invoke else statement
else:
    print("OMG!!!!")
