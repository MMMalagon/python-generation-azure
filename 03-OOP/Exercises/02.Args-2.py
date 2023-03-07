import random

'''
class CaseInsensitiveDict(dict):
    def __getitem__(self, key):
        return super().__getitem__(key.lower())
    
    def __setitem__(self, key, value):
        super().__setitem__(key.lower(), value)
        
    def __contains__(self, key):
        return super().__contains__(key.lower())
'''    

operators = {
    'sum': {
        'func': lambda a, b: a + b,
        'msg': 'plus'
    },
    'sub': {
        'func': lambda a, b: a - b,
        'msg': 'minus'
    },
    'mul': {
        'func': lambda a, b: a * b,
        'msg': 'multiplied by'
    },
    'div': {
        'func': lambda a, b: a / b,
        'msg': 'divided by'
    }    
}


def randomizer(min=0, max=10):
    return random.randint(min, max)


def calculate(*args):
    result = None

    try:
        integers = []
        strings = []

        if len(args) != 3:
            raise TypeError

        for arg in args:
            if type(arg) == int:
                if len(integers) == 2:
                    raise TypeError
                integers.append(arg)
            
            elif type(arg) == str:
                if len(strings) == 1:
                    raise TypeError
                strings.append(arg)
            
            else:
                raise TypeError

        """         
        if len(integers) != 2 or len(strings) != 1:
            raise TypeError
        """        

        result = operators[strings[0]]['func'](*integers)

    except ZeroDivisionError:
        print(f"{integers[0]} cannot be divided by {integers[1]}.")  # We could print directly zero
    except TypeError:
        print(f"Parameters must be: integer, integer, operator ({operators.keys()}). Args order is not in consideration.")
    except KeyError:
        print(f"Operation '{strings[0]}' is not recognised. Available operations: {operators.keys()}.")

    return result


def main():
    for operator in operators.keys():
        a, b = randomizer(), randomizer()
        result = calculate(*[a, operator, b])
        if result is not None:
            print(f"{a} {operators[operator]['msg']} {b} equals {float(result):.2g}")


if __name__ == "__main__":
    main()
