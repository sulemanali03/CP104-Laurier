"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-09"
-------------------------------------------------------
"""
# Imports

# Constants
cake_pieces = int(input("Number of pieces of cake:"))
party_goers = int(input("Number of party-goers:"))

cakes_recieved = cake_pieces//party_goers

not_distributed = cake_pieces % party_goers

print(f'Each party-goer recieves {cakes_recieved} pieces of cake ')
print(f'Pieces of cake that wont be distributed: {not_distributed}')
