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
from functions import customer_append
# Constants

with open('customers.txt', 'a') as fh:
    customer_append(fh, ['35612', 'David', 'Brown', 237.56, '2008-10-10'])

print('data appended to file')
