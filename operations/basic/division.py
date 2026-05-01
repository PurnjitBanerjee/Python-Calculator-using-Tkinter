def division():
    num1 = float(input("Enter the divident:"))
    num2 = float(input("Enter the divisor:"))
    if num2 != 0:
        print("Quotient is", num1 / num2, "Remeinder is", num1 % num2)
    else:
        print("Error! Division by zero is not allowed")
