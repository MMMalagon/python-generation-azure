def welcome(name: str = "Unknown") -> None:
    print(f"Welcome, {name}!")

my_name = 'Manuel'    
welcome(my_name)


demo = lambda name: print(f"Hello, I'm {name}!")
demo('Python')



def aggregate(num):
    return lambda a: a + num

def substrate(num):
    return lambda a: a - num

def multiply(num):
    return lambda a: a * num

def divide(num):
    return lambda a: a / num

def calculate(formula, value):
    print(f"Value: {value}")
    print(f"Result: {formula(value)}")

calculate(aggregate(25), 32)
calculate(substrate(25), 32)
calculate(multiply(25), 32)
calculate(divide(25), 32)

formula = lambda a: a / 12

calculate(formula, 32)

#######################################
def calculate(formula, *args):
    print(f"Values: {args}")
    print(f"Result: {formula(*args)}")

formula = lambda a, b: (a / 12) * b

calculate(formula, 32, 35)
calculate(formula, 32, 35)
# calculate(formula, 32)  # throws exception due to missing arg(s)
# calculate(formula, 32, 35, 38)  # throws exception due to too many args
#######################################

def calculate(formula):
    for n in range(1, 11, 1):
        print(f"Value {n} - Result: {formula(n)}")

calculate(divide(2))
calculate(lambda x: x - 1)
