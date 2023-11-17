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
from functions import level_of_pollution
# Constants

air_quality_index = int(input("Enter AQI: "))

level = level_of_pollution(air_quality_index)

print(level)
