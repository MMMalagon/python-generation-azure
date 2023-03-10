numbers = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

print(numbers)

def greater_than_hundred(numbers):
    result = []

    for number in numbers:
        if number > 100:
            result.append(number)

    return result

print(greater_than_hundred(numbers))

def func_1(x):
    if x > 100:
        return True
    else:
        return False
    
def func_2(x):
    return x % 2 == 0

print(list(filter(func_1, numbers)))
print(list(filter(func_2, numbers)))


func_1 = lambda x: x > 100
print(list(filter(func_1, numbers)))

print(list(filter(lambda x: x > 100, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))
print(list(filter(lambda x: x < 50, numbers)))

def custom_filter(func, iter):
    result = []

    for elem in iter:
        if func(elem):
            result.append(elem)

    return result

print(custom_filter(lambda x: x > 100, numbers))

###################################################
def custom_filter_v2(func, iter):
    return [elem for elem in iter if func(elem)]

print(custom_filter_v2(lambda x: x > 100, numbers))
###################################################
