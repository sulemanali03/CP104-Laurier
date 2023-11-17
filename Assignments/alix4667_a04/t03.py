"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
# Imports
from functions import largest_product
# Constants


val1 = float(input("Enter the first number: "))
val2 = float(input("Enter the second number: "))
val3 = float(input("Enter the third number: "))

product = (largest_product(val1, val2, val3))

print(product)
