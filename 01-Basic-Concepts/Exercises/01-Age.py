from dateutil.relativedelta import relativedelta
from datetime import datetime

import traceback

adult_age = 18

current_date = datetime.now().date()

while True:
    try:
        str_birth_date = input(
            "Insert your date of birth in the given form (DD-MM-YYYY) or press 'Q' to exit: ")
        if str_birth_date.upper() == 'Q':
            print("Exiting...")
            exit(0)
        birth_date = datetime.strptime(str_birth_date, "%d-%m-%Y").date()
    except ValueError as e:
        print("Incorrect date format. Please, review the input and try again.")
    except Exception as e:
        print("Some fatal error happened. Here is the error and the traceback:")
        print(e)
        traceback.print_exc()
        exit(1)
    else:
        break

# it seems to be not so precise
age = relativedelta(current_date, birth_date).years

if age < 0:
    print("Impossible, you have not been born yet!")
else:
    print(f"You're {age} years old.")
    if age < adult_age:
        print("You're underage.")
    else:
        print("You're an adult.")
