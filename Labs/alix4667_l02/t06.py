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

principle_amount = int(input("mortgage principle :"))
number_of_years = float(input("number of years:"))
interest_rate_percentage = float(input("Yearly interest rate :"))
number_of_months = number_of_years * 12
interest_rate = interest_rate_percentage / 100 / 12
numerator = interest_rate * ((1 + interest_rate) ** number_of_months)
denominator = ((1 + interest_rate) ** number_of_months) - 1
monthly_payment = principle_amount * numerator / denominator
print("The monthly payments are: $", monthly_payment)
