"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-24"
-------------------------------------------------------
"""
# Imports

# Constants


def list_of_factors(number):
    """
    -------------------------------------------------------
    Determines the factors of number.
    Use: li = list_of_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int > 1)
    Returns:
        li - list of factors (list int > 0)
    ------------------------------------------------------
    """
    factor = 1
    li = []

    while (number != 0) and (factor < number):
        if number % factor == 0:
            li.append(factor)
            factor += 1
        else:
            factor += 1

    return li


def list_of_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_of_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    user_input = int(input("Enter a positive number: "))
    number_list = []

    if user_input > 0:
        number_list.append(user_input)

    while user_input != 0:
        user_input = int(input("Enter a positive number: "))
        if user_input > 0:
            number_list.append(user_input)

    print()
    print(number_list)

    return number_list


def find_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = find_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    index_list = []

    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index_list.append(i)

    return index_list


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(subtrahend) + 1):

        for i in minuend:

            if i in subtrahend:
                minuend.remove(i)

    return


def check_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = check_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    min_num = numbers[0]

    for i in numbers:
        if i != 0:
            current_num = i
            if current_num < min_num:
                min_num = current_num

    if numbers[0] == min_num:
        in_order = True
        index = -1

    else:
        in_order = False
        index = min_num

    return in_order, index
