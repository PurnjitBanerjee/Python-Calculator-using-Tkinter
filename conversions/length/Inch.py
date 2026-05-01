def inch():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "yard":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 36, "yard")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 12, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 39.3701, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 * 2.54, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 * 25.4, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 39370.1, "km")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 * 25400, "micrometers")
    elif convertion_to == "mile":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 63360, "mile")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 * 25400000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of inches:"))
        print("Result is", num1 / 72913.4, "nautical miles")
    else:
        print("Invalid input")
