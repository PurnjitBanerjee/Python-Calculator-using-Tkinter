import math


def log():
    number = float(input("Enter the number: "))
    base = float(input("Enter the base: "))

    if number <= 0:
        print("Error! Number must be greater than zero")
        return
    if base <= 0:
        print("Error! Base must be greater than zero")
        return
    if base == 1:
        print("Error! Base cannot be 1")
        return

    print("The log value is", round(math.log(number, base), 3))
