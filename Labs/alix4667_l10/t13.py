"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
# Imports
from functions import file_copy
# Constants

fh_1 = open("words.txt", "r", encoding="utf-8")
fh_2 = open("new_words.txt", "w+", encoding="utf-8")

file_copy(fh_1, fh_2)
