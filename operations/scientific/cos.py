import math


def cos():
    angle_degrees = float(input("Enter the angle in degrees: "))
    n_terms = int(input("Enter the number of terms for approximation: "))
    x_radians = math.radians(angle_degrees)

    def taylor_cos(x, n_terms):
        cos_approx = 0
        for n in range(n_terms):
            cos_approx += ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        return cos_approx

    cos_value = taylor_cos(x_radians, n_terms)
    print("The cosine value for", angle_degrees, "is", round(cos_value, 3))
