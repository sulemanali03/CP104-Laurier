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

# Constants

from functions import linear_search

values = input("Enter a list of values: ")
value = int(input("Enter the value to find the index for: "))

index = linear_search(values, value)

print()
print(index)
