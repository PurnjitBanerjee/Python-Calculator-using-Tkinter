def yard():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 36, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 3, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 0.9144, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 91.44, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 914.4, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 / 1093.61, "km")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 914400, "micrometers")
    elif convertion_to == "mile":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 / 1760, "mile")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 * 914400000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of yards:"))
        print("Result is", num1 / 2025.37, "nautical miles")
    else:
        print("Invalid input")
