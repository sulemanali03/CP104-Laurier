"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports
from functions import statistics

# Constants


n = int(input("Enter the number of values: "))

print()
value = float(input("First value: "))

for values in range(n):
    next_value = float(input("Next value: "))
    value = next_value
    min_value, max_value, total = statistics(n)


print(min_value, max_value, total)
