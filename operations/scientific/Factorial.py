def frac():
    n = float(input("Enter the number you want factorial of"))
    f = 1
    if n == 1 or n == 0:
        print("Factorial is 1")
    else:
        for i in range(2, n + 1):
            f = f * i
        print("Factorial is", f)
