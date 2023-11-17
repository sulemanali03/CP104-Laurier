"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-09"
-------------------------------------------------------
"""
# Imports
from functions import lawn_mowing

# Constants

width = int(input("Width (m):"))
length = int(input("Length (m):"))
speed = int(input("Speed (m^2/minute):"))

print (f'lawn_mowning(width, length, speed) -> {lawn_mowing(width, length, speed)}')
