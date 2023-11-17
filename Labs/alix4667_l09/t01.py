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
from functions import is_hydroxide
# Constants


chemical = input("Enter a chemical formula:")

hydroxide = is_hydroxide(chemical)

print(hydroxide)
