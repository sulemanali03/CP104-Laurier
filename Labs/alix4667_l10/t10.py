"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-30"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word
# Constants

with open('words.txt', 'r') as fh:
    word = 'Exercise'
    count = count_frequency_word(fh, word)
    print(f"'{word}' appears {count} time(s)")
