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
from random import randint
import ast
# Constants


DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    return DAYS_OF_WEEK[d-1]


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    Requires import: from random import randint
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int, > 0)
        low - low value range (int)
        high - high value range (int, > low)
    Returns:
        values - a list of random integers (list of int)
    -------------------------------------------------------
    """
    values = []
    for i in range(n):
        value = randint(low, high)
        values.append(value)
    return values


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    largest = 0
    smallest = 0
    total = 0
    for i in range(len(values)):
        number = values[i]
        if i == 0 or number > largest:
            largest = number
        if i == 0 or number < smallest:
            smallest = number
        total += number
    average = total / len(values)
    return smallest, largest, total, average


def linear_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns its index.
    User: index = linear_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        index - the index of the location of value in values,
            -1 if not found (int).
    -------------------------------------------------------
    """

    li = ast.literal_eval(values)
    index = 0
    k = 0

    while index <= len(li):
        if value == li[index]:
            break
        index += 1
    while k <= len(li):
        k += 1
    if index == k:
        index = -1
    return index


def min_search(values):
    """
    -------------------------------------------------------
    Searches through values for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes values has at least
    one element.)
    User: indexes = min_search(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
    Returns:
        indexes - a list of indexes of the minimum values in
            values (list of int).
    -------------------------------------------------------
    """
    min_value = min(values)
    indexes = [i for i, v in enumerate(values) if v == min_value]
    return indexes
