numbers = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]


def demo_1(numbers):
    for number in numbers:
        return number * 5


def demo_2(numbers):
    new = []

    for number in numbers:
        new.append(number * 5)

    return new


def demo_3(numbers):
    for number in numbers:
        yield number * 5


print(f"Number: {demo_1(numbers)}")
print(f"Demo 1: {demo_1(numbers)}")
print(f"Demo 2: {demo_2(numbers)}")
print(f"Demo 3: {demo_3(numbers)}")

generator_1 = demo_3(numbers)

print(f"Demo 3 - gen1 (next1): {next(generator_1)}")
print(f"Demo 3 - gen1 (next2): {next(generator_1)}")
print(f"Demo 3 - gen1 (next3): {next(generator_1)}")

generator_2 = demo_3(numbers)

for number in generator_2:
    print(f"Demo 3 - gen2 (for loop): {number}")

for number in generator_1:
    print(f"Demo 3 - gen1 (for loop) - (starts late): {number}")

for number in generator_1:
    # shouldn't be printed
    print(f"Demo 3 - gen1 (for loop) - (already end): {number}")

list_demo_3 = list(demo_3(numbers))

for number in list_demo_3:
    print(f"Demo 3 - list (for loop) - Part 1: {number}")

for number in list_demo_3:
    print(f"Demo 3 - list (for loop) - Part 2: {number}")
