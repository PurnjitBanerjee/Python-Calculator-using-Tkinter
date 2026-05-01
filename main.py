# This a calculator that can perform addition, subtraction, multiplication, division, n'th root and power, Compound interest, length conversion(inches to cm,cm to inches,m to feet,etc.)
from conversions.length import Length_converter
from finance import Simple_interest, compound_interest
from operations.basic import difference, division, percent, percent2, product, sum
from operations.scientific import (
    Factorial,
    cos,
    cosec,
    cot,
    exponentiation,
    ln,
    log,
    root,
    sec,
    sin,
    tan,
)

print("'+'is for addition")
print("'-'is for substraction")
print("'x'is for multiplication")
print("'/'is for division")
print("'%'is for percent")
print("'per'is for amount from percent")
print("'Expo'is for exponentiation")
print("'Root'is for root of number")
print("'CI'is for compound interest")
print("'SI'is for Simple interest")
print("'LC'is for length conversion")
print("'Frac'is for Factorial")
print("'cos' is for Cosine")
print("'sin' is for Sine")
print("'tan' is for Tangent")
print("'sec' is for Secant")
print("'cosec' is for Cosecant")
print("'cot' is for Cotangent")
print("'log' is for Logarithm with base")
print("'ln' is for Natural logarithm")
print("'UI' is for calculator window")

opearator = str(input("Enter the opearation you want to perform:"))
if opearator == "+":
    sum.sum()
elif opearator == "-":
    difference.difference()
elif opearator == "x":
    product.product()
elif opearator == "/":
    division.division()
elif opearator == "Expo":
    exponentiation.expo()
elif opearator == "Root":
    root.root()
elif opearator == "CI":
    compound_interest.CI()
elif opearator == "SI":
    Simple_interest.SI()
elif opearator == "LC":
    Length_converter.LC()
elif opearator == "Frac":
    Factorial.frac()
elif opearator == "cos":
    cos.cos()
elif opearator == "sin":
    sin.sin()
elif opearator == "tan":
    tan.tan()
elif opearator == "sec":
    sec.sec()
elif opearator == "cosec":
    cosec.cosec()
elif opearator == "cot":
    cot.cot()
elif opearator == "log":
    log.log()
elif opearator == "ln":
    ln.ln()
elif opearator == "%":
    percent.percent()
elif opearator == "per":
    percent2.percent2()
elif opearator == "UI":
    from ui import calculator_ui

    calculator_ui.main()
else:
    print("Invalid operator")
