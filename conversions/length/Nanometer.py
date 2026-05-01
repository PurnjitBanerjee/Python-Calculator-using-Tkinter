def nano():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 25400000, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 304800000, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1000000000, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 10000000, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1000000, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1000000000000, "km")
    elif convertion_to == "miles":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1609344000000, "miles")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 914400000, "yards")
    elif convertion_to == "micrometers":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1000, "micrometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of nanometers:"))
        print("Result is", num1 / 1852000000000, "nautical miles")
    else:
        print("Invalid input")
