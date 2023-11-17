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

from functions import generate_integer_list

n = int(input("Enter the range of values: "))
low = int(input("Enter the lowest value: "))
high = int(input("Enter the highest value: "))

values = generate_integer_list(n, low, high)

print(values)
