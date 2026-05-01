import math


def ln():
    number = float(input("Enter the number: "))

    if number <= 0:
        print("Error! Number must be greater than zero")
        return

    print("The natural log value is", round(math.log(number), 3))
