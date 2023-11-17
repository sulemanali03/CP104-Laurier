"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-06-12"
-------------------------------------------------------
"""
# Imports

# Constants


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
    num - an integer (int > 0)
    Returns:
    total - sum of all even numbers from 2 to num (int)
     ------------------------------------------------------
    """

    total = 0
    for even_numbers in range(2, num + 1, 2):
        total += even_numbers

    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
    height - number of characters high (int > 0)
    width - number of characters wide (int > 0)
    char - the character to draw with (str, len() == 1)
    Returns:
    None
    ------------------------------------------------------
    """

    for i in range(height):

        print(char * width)

    return


def bottles_of_beer(n):
    """
    -------------------------------------------------------
    Prints n verses of the song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(n)
    -------------------------------------------------------Parameters:
    n - number of verses of the song to print (int > 0)
    Returns:
    None
    ------------------------------------------------------
    """
    bottles = 0
    for verses in range(n, 2, -1):
        bottles = verses
        print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
        bottles -= 1
        print(
            f"Take one down, pass it around, {bottles} bottles of beer on the wall.")
    print("2 bottles of beer on the wall, 2 bottles of beer.")
    print("Take one down, pass it around, 1 bottle of beer on the wall.")
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    return


def treadmill(burnt_per_minute, start, end, inc):
    """

    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
    burnt_per_minute - calories burnt per minute (float > 0)
    start - start time in minutes (int > 0)
    end - end time in minutes (int >= start)
    inc - increment in minutes (int > 0)
    Returns:
    None
    ------------------------------------------------------
    """
    for i in range(start, end+1, inc):

        calories_burnt = burnt_per_minute * i

        print(f"Calories burned after {i} minutes: {calories_burnt:.1f}")

    return


def statistics(n):
    """

    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
    n - number of values to process (int > 0)
    Returns:
    minimum - smallest of n values (float)
    maximum - largest of n values (float)
    total - total of n values (float)
    average - average of n values (float)
    ------------------------------------------------------
    """

    total = 0
    for values in range(0, n):
        min_value = min(n[values])
        max_value = max(n[values])
        total += values
    return min_value, max_value, total
