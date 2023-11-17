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
from functions import colour_mix
# Constants


rgb_colour1 = input("Enter first primary colour: ")
rgb_colour2 = input("Enter second primary colour: ")

colour = colour_mix(rgb_colour1, rgb_colour2)

print(colour)
