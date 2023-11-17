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
from functions import find_indexes, list_of_positives

# Constants


numbers = list_of_positives()
target_number = int(input("Enter the number to find the index for: "))

index_list = find_indexes(numbers, target_number)


print(index_list)
