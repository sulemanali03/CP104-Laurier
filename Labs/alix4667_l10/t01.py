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
from functions import customer_record
# Constants

fh = open("customers.txt", "r", encoding="utf-8")

n = int(input("Enter a record number: "))

result = customer_record(fh, n)

fh.close()

print(result)
