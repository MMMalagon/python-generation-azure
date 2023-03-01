# Data type conversion

a = 5
b = "25"
c = "25.7"

# throws an exception because it's not possible to concatenate an string with a different data type
# print("Number: " + a)

print("Number: " + str(a))

# converts implicity to str (take a look at the comma - it's concatenating under the hood with a separator which is a space by default)
print("Number:", a)

print(int(b))
print(b + c)

print(int(b) + float(c))
print(type(int(b) + float(c)))

# thows an exception due to be a float var, not an int (base 10)
# print(int(b) + int(c))

print(int(b) + int(float(c)))
print(type(int(b) + int(float(c))))

print(int(b) + round(float(c)))
