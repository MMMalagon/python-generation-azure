# First try
a = 5
b = 10

a = b
b = a

print("First try: Incorrect assigment")
print(a)
print(b)


# Second try

a = 5
b = 10

tmp = a
a = b
b = tmp

print("Second try: Corrent assigment using temporal variable")
print(a)
print(b)


# Third try

a = 5
b = 10

a, b = b, a

print("Third try: Corrent assigment using simultaneous assigment")
print(a)
print(b)
