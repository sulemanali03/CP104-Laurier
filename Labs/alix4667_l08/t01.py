"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-14"
-------------------------------------------------------
"""
# Imports
from functions import get_weekday_name
# Constants

for i in range(1, 8):
    day_name = get_weekday_name(i)
    print(f"{i} = {day_name}")

d = int(input("Enter day:"))
name = (get_weekday_name(d))
print(name)
