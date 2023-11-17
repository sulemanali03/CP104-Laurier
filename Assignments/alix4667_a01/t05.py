"""
-------------------------------------------------------
[program description]
--------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-01-30"
-------------------------------------------------------
"""
# Imports

# Constants

principle_amount = float(input("Principle:"))
interest = float(input("Interest:"))
number_of_years = int(input("Number of years:"))
interest_compounded_per_year = int(
    input("Number of times interest compounded per year:"))
interest_decimal = interest/100
money_accumulated = principle_amount * \
    ((1 + (interest_decimal/interest_compounded_per_year))
     ** (interest_compounded_per_year * number_of_years))

print("Balance: $", money_accumulated)
