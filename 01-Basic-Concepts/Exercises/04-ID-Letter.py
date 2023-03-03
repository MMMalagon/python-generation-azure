import traceback


letters = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X',
           'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']

divisor = len(letters)

while True:
    try:
        id_str = input(
            "Insert your ID (without the letter) or press 'Q' to exit: ")
        if id_str.upper() == 'Q':
            print("Exiting...")
            exit(0)
        id_num = int(id_str)
        if id_num < 0 or id_num > 99999999:
            raise ValueError
    except ValueError as e:
        print(
            "Incorrect input format. The ID must be an integer between 0 and 99999999 and without the letter.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break

id_letter = letters[id_num % divisor]

print(
    f"Your ID letter is '{id_letter}', so your complete ID is '{str(id_num).zfill(8)}-{id_letter}'")
