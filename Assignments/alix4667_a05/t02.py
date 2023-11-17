"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""
# Imports
from functions import cal_burned
# Constants

per_min = float(input("Enter the number of calories burned per minute: "))
minutes = int(input("Enter the number of minutes ran: "))

total_calories = cal_burned(per_min, minutes)
