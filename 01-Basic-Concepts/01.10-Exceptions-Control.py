import traceback
from pathlib import Path
# from os.path import isfile

n1 = 100
n2 = 1
f1 = './file.txt'

print(f"We're going to try to divide {n1} by {n2}:")

try:
    n3 = n1 / n2
    # assert isfile(f1)  #AssertionError
    path_f1 = Path(f1)
    path_f1.resolve(strict=True)  # FileNotFoundError
    with open(f1, encoding="utf8", mode="a") as f:
        f.writelines(f"{str(n3)}\n")
except ZeroDivisionError as e:
    print()
    print("Go back to primary school, please!")
    # raise(e)
except FileNotFoundError:
    print()
    print("I'm unable to open the given file to store the result... Bro, this is sus... ඞ")
except Exception as e:
    print()
    print("A wild fatal error appeared! Here it is:")
    print()
    print(e)
    print()
    print("And now the TL;DR traceback, just in case you need it:")
    print()
    traceback.print_exc()
else:
    print()
    print(f"Equals: {n3:.2f}")
finally:
    print()
    print("Bye!")
