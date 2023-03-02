for i in range(0, 10):
    print(i)

for i in range(9, -1, -1):
    print(i)

'''
    for i in range(0.0, 1.1, 0.1): # this doesn't work
        print(i)

    [x * 0.1 for x in range(0, 10)]

    xs = (x * 0.1 for x in range(0, 10))
'''

factor = 0.1

xs = (x * factor for x in range(int(0 / factor), int(1 / factor)))
for x in xs:
    print(f"{x:.1f}")


citrus_fruits = ["orange", "lemon", "grapefruit", "lime", "tangerine"]

print(citrus_fruits)
print(citrus_fruits[3])
print(f"Total lenght: {len(citrus_fruits)}")
print()

for x in range(0, 4, 1):
    print(f"{x}: {citrus_fruits[x]}")

print()

for x in range(0, len(citrus_fruits), 1):
    print(f"{x}: {citrus_fruits[x]}")

print()

for fruit in citrus_fruits:
    print(fruit)

print()

for idx, fruit in enumerate(citrus_fruits):
    print(f"{idx}: {fruit}")

print()

for i in range(10):
    if i == 4:
        continue
    if i == 7:
        break
    print(i)
