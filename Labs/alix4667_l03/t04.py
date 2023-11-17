"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports

# Constants

number = float(input("Enter a number:"))
percent = float(input("Enter percent:"))
discount = percent/100 * number
print(f"A {percent:.1f} discount on {number} is {discount:.1f}")
