def nat_miles():
    convertion_to = str(input("Enter the unit you want to convert to:"))
    if convertion_to == "inch":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 72913.4, "inch")
    elif convertion_to == "foot":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 6076.12, "foot")
    elif convertion_to == "m":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 1852, "m")
    elif convertion_to == "cm":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 185200, "cm")
    elif convertion_to == "mm":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 1852000, "mm")
    elif convertion_to == "km":
        num1 = float(input("Enter the number of Nautical Miles:"))
        print("Result is", num1 * 1.852, "km")
    elif convertion_to == "miles":
        num1 = float(input("Enter the number of Nautical miles:"))
        print("Result is", num1 * 1.15078, "mile")
    elif convertion_to == "yards":
        num1 = float(input("Enter the number of Nautical miles:"))
        print("Result is", num1 * 2025.37, "yards")
    elif convertion_to == "nano":
        num1 = float(input("Enter the number of Nautical miles:"))
        print("Result is", num1 * 1852000000000, "nanometers")
    elif convertion_to == "micro":
        num1 = float(input("Enter the number of Nautical miles:"))
        print("Result is", num1 * 1852000000, "micrometer")
    else:
        print("Invalid input")
