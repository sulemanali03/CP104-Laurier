"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports

# Constants

date = int(input("Enter a date in the format DDMMYY:"))

day = date // 1000000

month = (date // 10000) % 100

year = date % 10000

print(f'The reformatted date: {year:04d}/{month:02d}/{day:02d}')
