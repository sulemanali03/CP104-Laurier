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
from functions import employee_payroll
# Constants

total, average = employee_payroll()
print(f"\nTotal net employee wages: ${total:,.2f}")
print(f"Average employee net wages: ${average:,.2f}")
