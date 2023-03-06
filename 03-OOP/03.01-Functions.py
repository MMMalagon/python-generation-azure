from datetime import datetime

# Example of a function that does have no parameters (does not receive data) and does not return any data
def func_1():
    print("Hello everyone!")


# Example of a function that does have parameters (does receive data) and does not return any data
def func_2(name, number):
    print(f"Hi, I'm {name} and my lucky number is {number}.")


# Example of a function that does have parameters (does receive data) and does return data
def func_3(phrase):
    length = 0
    length = len(phrase)
    return length


# Example of a function that does have no parameters (does not receive data) and does return data
def func_4():
    return datetime.now().date().strftime("%A")


func_1()

func_2("Manuel", 61)

print(func_3("Hello everyone"))

data = func_3("Hello everyone")
print(f"Data: {data}")

print(func_4())

data_2 = func_4()
print(f"Data: {data_2}")
