"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-04-16"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants

SQUARE_FEET_PER_ACRE = 43560


def footage_to_acres(square_feet):
    """
    -------------------------------------------------------
    Converts square footage to acres.
    Use: acres = footage_to_acres(square_feet)
    -------------------------------------------------------
    Parameters:
        square_feet - area in square feet (float >= 0)
    Returns:
        acres - square_footage in acres (float)
    ------------------------------------------------------
    """
    acres = square_feet / SQUARE_FEET_PER_ACRE
    return acres


def lawn_mowing(width, length, speed):
    """
    -------------------------------------------------------
    Determines how long it takes to mow a rectangular lawn.
    Use: time = lawn_mowing(width, length, speed)
    -------------------------------------------------------
    Parameters:
        width - width of a lawn in metres (float > 0)
        length - length of a lawn in metres (float > 0)
        speed - square metres cut per minute (float > 0)
    Returns:
        time_minutes - time required to mow the lawn (float)
    ------------------------------------------------------
    """

    area = width * length
    time = area / speed
    return time


def date_extraction(date_number_format):
    """
    -------------------------------------------------------
    Extracts the year, month, and day from a date number in the format MMDDYYYY.
    Use: year, month, day = date_extraction(date_number_format)
    -------------------------------------------------------
    Parameters:
        date_number_format - a date number in the format MMDDYYYY (int > 0)
    Returns:
        year - year portion of date_number (int)
        month - month portion of date_number (int)
        day - day portion of date_number (int)
    ------------------------------------------------------
    """
    year = date_number_format % 10000

    month = date_number_format // 1000000

    day = (date_number_format // 10000) % 100

    return year, month, day


def fraction_multiplier(number1, denom1, number2, denom2):
    """
    -------------------------------------------------------
    Multiplies two fractions together and returns the results
    Use: num, denom, product = fraction_multiplier(number1, denom1, number2, denom2)
    -------------------------------------------------------
    Parameters:
        number1 - numerator of the first fraction (int)
        denom1 - denominator of the first fraction (int)
        number2 - numerator of the second fraction (int)
        denom2 - denominator of the second fraction (int)
    Returns:
        num - numerator of the resulting fraction (int)
        denom - denominator of the resulting fraction  (int)
        product - numerator divided by denominator (float)
    ------------------------------------------------------
    """

    a = number1 * number2

    b = denom1 * denom2

    c = a/b

    return a, b, c


def math_quiz():
    """
    ----------------------------------------------
    Display two random numbers between 0 and 999 that are to be added and ask a user to enter alomng the expected answer
    Use: result= math_quiz()
    ----------------------------------------------
    Parameters:
       None
    Returns:
       None
    ----------------------------------------------
    """

    number1 = randint(0, 999)
    number2 = randint(0, 999)

    answer = number1 + number2

    print(f'{number1}')

    print(f'+ {number2}')

    your_answer = int(input("Your answer: "))

    print(f'Your answer:{your_answer}')

    print(f"Expected answer: {answer}")
    return
