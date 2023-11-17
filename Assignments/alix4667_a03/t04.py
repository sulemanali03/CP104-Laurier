"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
# Imports
from functions import fraction_multiplier
# Constants

number1 = int(input("Numerator 1:"))
denom1 = int(input("Denominator 1:"))
number2 = int(input("Numerator 2:"))
denom2 = int(input("Denominator 2:"))

a, b, c = fraction_multiplier(number1, denom1, number2, denom2)

print(f'fraction_multiplier(number1, denom1, number2, denom2))->{a}, {b}, {c}')
