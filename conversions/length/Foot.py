def foot():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "yard":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 / 3, "yard")
    elif convertion_to == "inch":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 * 12, "inch")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 / 3.28084, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 * 30.48, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 * 304.8, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 / 3280.84, "km")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 * 304800, "micrometers")
    elif convertion_to == "mile":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 / 5280, "mile")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 * 304800000, "nanometers")
    elif convertion_to == "nat. miles":
        num1 = float(input("Enter the number of feet:"))
        print("Result is", num1 / 6076.12, "nautical miles")
    else:
        print("Invalid input")
