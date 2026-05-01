import math


def taylor_cos(x, n_terms):
    cos_approx = 0
    for n in range(n_terms):
        cos_approx += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
    return cos_approx


def taylor_sin(x, n_terms):
    sine_approx = 0
    for n in range(n_terms):
        sine_approx += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
    return sine_approx


def cot():
    angle_degrees = float(input("Enter the angle in degrees: "))
    n_terms = int(input("Enter the number of terms for approximation: "))
    if n_terms <= 0:
        print("Error! Number of terms must be greater than zero")
        return

    x_radians = math.radians(angle_degrees)
    sin_value = taylor_sin(x_radians, n_terms)
    if round(sin_value, 12) == 0:
        print("Error! Cotangent is undefined for this angle")
        return

    cot_value = taylor_cos(x_radians, n_terms) / sin_value
    print("The cotangent value for", angle_degrees, "is", round(cot_value, 3))
