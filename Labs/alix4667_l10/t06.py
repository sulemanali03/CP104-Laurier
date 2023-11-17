"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
# Imports
from functions import number_stats
# Constants

with open('numbers.txt', 'r') as fh:

    smallest, largest, total, average = number_stats(fh)

    print(f'Smallest: {smallest}')
    print(f'Largest: {largest}')
    print(f'Total: {total:.2f}')
    print(f'Average: {average:.2f}')
