def SI():
    principle = float(input("Enter the principle:"))
    rate = float(input("Enter the rate of interest:"))
    time = float(input("Enter the time:"))
    print(
        "The amount is",
        ((principle * rate * time) / 100),
        "and interest is",
        (((principle * rate * time) / 100) - principle),
    )
