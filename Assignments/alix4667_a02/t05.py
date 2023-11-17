"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-02-07"
-------------------------------------------------------
"""
# Imports

# Constants

foundation_length = float(input("Foundation length (m):"))
foundation_width = float(input("Foundation width (m):"))
foundation_height = float(input("Foundation height (m):"))
wall_height = float(input("Wall height (m):"))
concrete = float(input("Cost of concrete ($/m^3):"))
bricks = float(input("Cost of bricks ($/m^2):"))

concrete_needed = foundation_length * foundation_width * foundation_height

concrete_cost = concrete_needed * concrete

area1 = (foundation_length * wall_height) * 2
area2 = (foundation_width * wall_height) * 2

bricks_needed = (area1 + area2)

bricks_cost = bricks_needed * bricks
total_cost = bricks_cost + concrete_cost


print(f'Concrete needed for foundation (m^3):{concrete_needed:,.2f}')
print(f'Cost of concrete:${concrete_cost:,.2f}')
print(f'Bricks needed for walls (m^2):{bricks_needed:,.2f}')
print(f'Cost of bricks:${bricks_cost:,.2f}')

print(f'Total cost: $ {total_cost}')
