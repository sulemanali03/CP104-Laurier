"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-29"
-------------------------------------------------------
"""
# Imports
from functions import draw_rectangle

# Constants

print("This Program prints a rectangle of height and width characters using a specific character.")

char_height = int(input("Enter the number of characters height: "))

char_width = int(input("Enter the number of characters wide: "))

char_char = str(input("Enter the character to draw with: "))

print()

draw_rectangle(char_height, char_width, char_char)
