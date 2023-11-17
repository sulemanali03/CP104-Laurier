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
from functions import day_of_the_week
# Constants

day_number = int(input("Please enter a number between 1 and 7: "))

day = day_of_the_week(day_number)

print(day)
