"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-07"
-------------------------------------------------------
"""
# Imports
from functions import treadmill

# Constants

print("Calculates and prints calories burnt on a treadmill over a given time range.")

calories_burnt_per_minute = float(input("calories burnt per minute: "))

start_time = int(input("start time in minutes: "))

end_time = int(input("end time in minutes: "))

increment = int(input("increment in minutes: "))

print()

treadmill(calories_burnt_per_minute, start_time, end_time, increment)
