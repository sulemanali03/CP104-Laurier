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
from functions import list_stats
# Constants


values = input("Enter the list of values: ")

smallest, largest, total, average = list_stats(values)

print()
print(smallest, largest, total, average)
