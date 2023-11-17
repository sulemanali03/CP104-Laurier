"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-17"
-------------------------------------------------------
"""
# Imports
from functions import date_extraction

# Constants

date = int(input("Enter a date in the format MMDDYYYY:"))

year, month, day = date_extraction(date)


print(f'date_extraction(date)->{year}, {month}, {day}')
