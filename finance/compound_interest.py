def CI():
    principal = float(input("Enter the principal amount:"))
    rate = float(input("Enter the rate of interest:"))
    time = float(input("Enter the time in years:"))
    frequency = float(input("Enter the frequenct"))
    CI = principal * (1 + (rate / (100 * frequency))) ** (time * frequency)
    print("Amuont is", CI, "and interest is", CI - principal)
