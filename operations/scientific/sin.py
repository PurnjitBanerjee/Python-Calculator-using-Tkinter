import math


def sin():
    angle_degrees = float(input("Enter the angle in degrees: "))
    n_terms = int(input("Enter the number of terms for approximation: "))
    x_radians = math.radians(angle_degrees)

    def taylor_sin(x, n_terms):
        sine_approx = 0
        for n in range(n_terms):
            sine_approx += ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        return sine_approx

    sin_value = taylor_sin(x_radians, n_terms)
    print("The sine value for", angle_degrees, "is", round(sin_value, 3))
