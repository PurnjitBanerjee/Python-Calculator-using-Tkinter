def cm():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 2.54, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 30.48, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 100, "m")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 * 10, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 100000, "km")
    elif convertion_to == "miles":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 160934.4, "miles")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 91.44, "yards")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 * 10000, "micrometers")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 * 10000000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of cm:"))
        print("Result is", num1 / 185200, "nautical miles")
    else:
        print("Invalid input")
