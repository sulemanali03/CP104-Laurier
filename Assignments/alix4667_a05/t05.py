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
from functions import total_range
# Constants


start_value = int(input("Enter value to start from: "))
increment = int(input("Enter the value for increments: "))
count = int(input("Enter the number of values: "))

total = total_range(start_value, increment, count)

print()
print(total)
