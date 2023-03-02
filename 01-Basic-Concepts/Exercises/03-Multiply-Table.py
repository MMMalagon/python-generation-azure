import traceback


while True:
    try:
        multiply_str = input("Insert the number: ")
        multiply = int(multiply_str)
        assert multiply >= 1 and multiply <= 10
    except AssertionError as e:
        print("Input value must be bewtween 1 and 10. Try again.")
    except ValueError as e:
        print("Incorrect integer format. Please, review the input and try again.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break

# for

for i in range(0, 11):
    print(f"{multiply}x{i}: {multiply*i}")


# while

i = 0

while (i <= 10):
    print(f"{multiply}x{i}: {multiply*i}")
    i += 1
