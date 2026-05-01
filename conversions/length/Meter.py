def m():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 39.3701, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 3.28084, "foot")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 / 1000, "km")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 1000, "mm")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 100, "cm")
    elif convertion_to == "mile":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 0.000621371, "mile")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 1.09361, "yards")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 1000000, "micro")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 1000000000, "nano")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of m:"))
        print("Result is", num1 * 0.0005399568, "nat. miles")
    else:
        print("Invalid input")
