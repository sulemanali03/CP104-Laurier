"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-11"
-------------------------------------------------------
"""
# Imports
from functions import meal_costs
# Constants

b_total, l_total, s_total, a_total = meal_costs()

print(f"\nTotal breakfast cost: ${b_total:.2f}")
print(f"Total lunches cost: ${l_total:.2f}")
print(f"Total suppers cost: ${s_total:.2f}")
print(f"Total meals cost: ${a_total:.2f}")
