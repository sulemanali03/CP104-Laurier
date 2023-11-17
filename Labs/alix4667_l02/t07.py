"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-01-25"
-------------------------------------------------------
"""
# Imports

# Constants

flyers = int(input("Number of flyers:"))
volunteers = int(input("Number of volunteers:"))
flyers_per_volunteers = flyers // volunteers
flyers_left_over = flyers % volunteers

print("Flyers per volunteers:", flyers_per_volunteers)
print("Flyers left over:", flyers_left_over)
