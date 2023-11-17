"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-27"
-------------------------------------------------------
"""
# Imports

# Constants
ANNUAL_TAX = 18.5

total_sales = int(input("Enter the total sales:"))

tax = ANNUAL_TAX/100 * total_sales

print("Projected Tax Report")

print("------------------------")

print(f'Total sales: $ {total_sales:,.2f}')

print(f'Annual tax:  % {ANNUAL_TAX:,.2f}')

print("------------------------")

print(f'Tax:         $ {tax:,.2f}')
