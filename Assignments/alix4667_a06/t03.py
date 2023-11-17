"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-14"
-------------------------------------------------------
"""
# Imports
from functions import interest_data
# Constants

principal_amount = float(input("Principal: $"))
interest_rate = float(input("Interest rate (%): "))
payment = float(input("Monthly payment: $"))

interest_data(principal_amount, interest_rate, payment)
