def micro():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 25400, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 304800, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 1000000, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 10000, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 1000, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 1000000000, "km")
    elif convertion_to == "miles":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 160934400, "miles")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 914400, "yards")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 * 1000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of micrometers:"))
        print("Result is", num1 / 1852000000, "nautical miles")
    else:
        print("Invalid input")
