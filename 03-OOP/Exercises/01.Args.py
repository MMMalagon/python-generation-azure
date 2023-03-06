import random


operators = ['sum', 'sub', 'div', 'mul']


def randomizer(min=0, max=10):
    return random.randint(min, max)


def operators_strings(operator):
    strings = {
        'sum': 'plus',
        'sub': 'minus',
        'div': 'divided by',
        'mul': 'multiplied by',
    }
    return strings[operator]


def calculate(*args):
    result = None

    try:
        a, b, op = int(args[0]), int(args[1]), str(args[2])

        if op == 'sum':
            result = a + b
        elif op == 'sub':
            result = a - b
        elif op == 'div':
            result = a / b
        elif op == 'mul':
            result = a * b
        else:
            raise NotImplementedError

    except ZeroDivisionError:
        print(f"{a} cannot be divided by {b}.")
    except IndexError:
        print("Not enough arguments.")
    except TypeError:
        print("Parameters must be: integer, integer, string (sum, sub, div, mul).")
    except NotImplementedError:
        print(f"Operation '{op}' is not recognised. Available operations: {operators}.")

    return result


def main():
    for operator in operators:
        a, b = randomizer(), randomizer()
        result = calculate(*[a, b, operator])
        if result is not None:
            print(f"{a} {operators_strings(operator)} {b} equals {float(result):.2g}")


if __name__ == "__main__":
    main()
