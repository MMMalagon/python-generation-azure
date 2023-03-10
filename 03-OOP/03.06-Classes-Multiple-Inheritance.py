class A:
    number_1 = None
    number_2 = None

    def __init__(self) -> None:
        print("A >> builder")

    def add(self) -> int:
        return "A >> " + str(self.number_1 + self.number_2)

    def sub(self) -> int:
        return "A >> " + str(self.number_1 - self.number_2)


class B:
    number_1 = None
    number_2 = None

    def __init__(self, n1, n2) -> None:
        self.number_1 = n1
        self.number_2 = n2
        print("B >> builder")

    def add(self) -> int:
        return "B >> " + str(self.number_1 + self.number_2)

    def mul(self) -> int:
        return "B >> " + str(self.number_1 * self.number_2)


# For defined methods sharing the same name, those defined earlier
# (from left to right) will prevail (this also applies for constructors).
#
# In other words, it resembles the operation of multiple inheritance
# through interfaces in OOP languages such as Java.
#
# Be careful with attribute names (for example, if different between
# classes, some method won't work at all, or if they have different
# values on those different attributes, results will be different).
class Calculator(A, B):
    pass


c = Calculator()
c.number_1 = 78
c.number_2 = 15
print(f"Number 1: {c.number_1}")
print(f"Number 2: {c.number_2}")
print(f"Addition: {c.add()}")
print(f"Subtraction: {c.sub()}")
print(f"Multiplication: {c.mul()}")
