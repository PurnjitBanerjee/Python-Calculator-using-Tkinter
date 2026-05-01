import math


def taylor_cos(x, n_terms):
    cos_approx = 0
    for n in range(n_terms):
        cos_approx += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    return cos_approx


def sec():
    angle_degrees = float(input("Enter the angle in degrees: "))
    n_terms = int(input("Enter the number of terms for approximation: "))
    if n_terms <= 0:
        print("Error! Number of terms must be greater than zero")
        return

    x_radians = math.radians(angle_degrees)
    cos_value = taylor_cos(x_radians, n_terms)
    if round(cos_value, 12) == 0:
        print("Error! Secant is undefined for this angle")
        return

    print("The secant value for", angle_degrees, "is", round(1 / cos_value, 3))
