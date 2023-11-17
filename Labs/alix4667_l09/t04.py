"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-25"
-------------------------------------------------------
"""
# Imports
from functions import validate_code
# Constants


product_code = input("Enter product code:")

category, digits, qualifiers = validate_code(product_code)

print(validate_code(product_code))
