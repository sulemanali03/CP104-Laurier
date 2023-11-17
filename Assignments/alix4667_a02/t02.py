"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-05-09"
-------------------------------------------------------
"""
# Imports

# Constants


two_digits_number = int(input("Enter a positive digit number:", ))

tenths_number = two_digits_number//10

ones_number = two_digits_number % 10

product = tenths_number * ones_number

print(f'The product of the digits of {two_digits_number} is {product}')
