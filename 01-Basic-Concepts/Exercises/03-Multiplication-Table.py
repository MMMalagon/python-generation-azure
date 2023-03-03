import traceback


while True:
    try:
        multiply_str = input(
            "Insert a number between 1 and 10 or press 'Q' to exit: ")
        if multiply_str.upper() == 'Q':
            print("Exiting...")
            exit(0)
        multiply = int(multiply_str)
        if multiply < 1 or multiply > 10:
            raise ValueError
    except ValueError as e:
        print("Incorrect input format. The input must be an integer between 1 and 10.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break


# for

print("Multiply table using a FOR loop:")

for i in range(0, 11):
    print(f"{multiply}x{i}: {multiply*i}")


# while

print("Multiply table using a WHILE loop:")

i = 0

while (i <= 10):
    print(f"{multiply}x{i}: {multiply*i}")
    i += 1
