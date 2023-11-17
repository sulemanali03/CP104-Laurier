"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Imports
from functions import check_sorted, list_of_positives
# Constants

numbers = list_of_positives()

in_order, index = check_sorted(numbers)


print(f'{in_order}, {index}')
