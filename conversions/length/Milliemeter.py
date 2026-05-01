def mm():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 25.4, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 304.8, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 1000, "m")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 1000000, "km")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 10, "cm")
    elif convertion_to == "mile":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 1609344, "mile")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 914.4, "yards")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 * 1000, "micro")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 * 1000000, "nano")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of mm:"))
        print("Result is", num1 / 1852000, "nat. miles")
    else:
        print("Invalid input")
