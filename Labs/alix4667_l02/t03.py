"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-04-15"
-------------------------------------------------------
"""
# Imports

# Constants
LARGE_DOGS = 75
SMALL_DOGS = 50

l_dogs = int(input("Number of large dogs groomed:"))
s_dogs = int(input("Number of small dogs groomed:"))
total = LARGE_DOGS * l_dogs + SMALL_DOGS * s_dogs
print("Total earned for the day: $", total)
