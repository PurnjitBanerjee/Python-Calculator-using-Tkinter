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


def tan():
    angle_degrees = float(input("Enter the angle in degrees: "))
    n_terms = int(input("Enter the number of terms for approximation: "))
    x_radians = math.radians(angle_degrees)

    def taylor_tan(x, n_terms):
        cos_approx = taylor_cos(x, n_terms)
        if cos_approx == 0:
            return None  # Avoid division by zero
        return taylor_sin(x, n_terms) / cos_approx

    print(
        "The tangent value for",
        angle_degrees,
        "is",
        round(taylor_tan(x_radians, n_terms), 3),
    )
