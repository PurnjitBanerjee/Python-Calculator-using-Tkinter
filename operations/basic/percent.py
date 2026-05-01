def percent():
    x = float(input("Enter the no. you want percent of:"))
    y = float(input("Enter the ase no.:"))
    per = (x / y) * 100
    per = round(per)
    return per
    print("The percentage is", per)
