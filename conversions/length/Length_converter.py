from . import (
    Foot,
    Inch,
    Kilometer,
    Meter,
    Micrometer,
    Mile,
    Milliemeter,
    Nanometer,
    Nautical_Miles,
    Yard,
    centimeter,
)


def LC():
    print("'km' is for kilometer")
    print("'cm is for centimeter'")
    print("'m' is for meter")
    print("'foot' is for foot")
    print("'inch' is for inch")
    print("'yard' is for yard")
    print("'mm' is for milimeter")
    print("'micro' is for micrometer")
    print("'mile' is for mile")
    print("'nat. miles' is for nautical mile")
    print("'nano' is for nanometers")
    convertion_from = str(input("Enter the unit you want to convert from:"))
    if convertion_from == "km":
        Kilometer.km()
    elif convertion_from == "m":
        Meter.m()
    elif convertion_from == "mm":
        Milliemeter.mm()
    elif convertion_from == "cm":
        centimeter.cm()
    elif convertion_from == "micro":
        Micrometer.micro()
    elif convertion_from == "nano":
        Nanometer.nano()
    elif convertion_from == "mile":
        Mile.mile()
    elif convertion_from == "yard":
        Yard.yard()
    elif convertion_from == "foot":
        Foot.foot()
    elif convertion_from == "inch":
        Inch.inch()
    elif convertion_from == "nat. miles":
        Nautical_Miles.nat_miles()
    else:
        print("Not available")
