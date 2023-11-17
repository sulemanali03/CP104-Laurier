"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-16"
-------------------------------------------------------
"""
# Imports
from functions import footage_to_acres

# Constants

square_feet = float(input("Square footage:"))

acres = footage_to_acres(square_feet)


print(f'{square_feet} -> {acres}')
