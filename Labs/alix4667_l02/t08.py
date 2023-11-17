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

height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))
bmi_upper_limit = int(input("Enter your upper limit BMI:"))

Body_Mass_Index = weight/(height**2)
BMI_Prime = Body_Mass_Index/bmi_upper_limit
print("Body Mass Index (kg/m^2) = ", Body_Mass_Index)
print("BMI Prime = ", BMI_Prime)
