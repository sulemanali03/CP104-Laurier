"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-01-27"
-------------------------------------------------------
"""
# Imports

# Constants

breakfast = float(input("Enter cost of breakfast:"))
lunch = float(input("Enter cost of lunch:"))
supper = float(input("Enter cost of supper:"))
total = float(breakfast+lunch+supper)
print(f'Meal        Cost')


print(f"Breakfast   ${breakfast:6.2f}")
print(f"Lunch       ${lunch:6.2f}")
print(f"Supper      ${supper:6.2f}")
print(f"Total       ${total:6.2f}")
