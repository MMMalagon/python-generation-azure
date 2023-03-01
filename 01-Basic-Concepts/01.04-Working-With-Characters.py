string = "Hello World!"

print(string)
print(string[2])
print(string[2:])
print(string[:6])
print(string[2:6])
print(string[-2])
print(string[-6:])
print(string[:-1])
print(len(string))


print(string.lower())
print(string.upper())
print(string.capitalize())
print(string.replace("o", "0"))
print(string.isdigit())
print("33".isdigit()) # int, float...
print("33".isdecimal()) # only numbers
print("33.3".isdigit()) 
print("33.3".isdecimal()) # even if it's a digit, because it has a decimal point, it's not detected as a decimal (quite contradictory)
print(string.count("o"))
print(string.count("")) # it counts one more than len() function (it's counting like empty strings, if that makes sense, so maybe the null var that flags the string end it's counted)
print(string.strip("!"))
print('     LOL     '.strip()) # removes the specified char (or chars) at the beginning or the end of the string (defaults to space)
print(string.split("o"))


# message = "World"
message = input()

print("Hello " + message + "!")
print("Hello {}!".format(message))
print("Hello {s}!".format(s=message))
print(f"Hello {message}!")

print("Hello " + message + " " + string + "!")
print("Hello {s} {c}!".format(s=message, c=string))
print(f"Hello {message} {string}!")

result = "Hello {s}!".format(s=message)
# result = f"Hello {message}!"
print(result)

number = 10 / 3
print(number)
print("Number: {n}".format(n=number))
print("Number: {n:1.4f}".format(n=number))
