def mile():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 63360, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 5280, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1609.34, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 160934, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1609344, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1.60934, "km")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1609344000, "micrometers")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1760, "yards")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 1609344000000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of miles:"))
        print("Result is", num1 * 0.868976, "nautical miles")
    else:
        print("Invalid input")
