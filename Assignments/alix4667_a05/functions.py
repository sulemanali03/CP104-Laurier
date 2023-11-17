"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-10"
-------------------------------------------------------
"""
# Imports

# Constants


def factorial_calculator(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = factorial_calculator(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


def cal_burned(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates the amount of calories burned every five
    minutes and prints a table 
    Use: total_calories = cal_burned(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (float > 0)
        minutes - total minutes ran on the treadmill (int > 0)
    Returns:
    None
    ------------------------------------------------------
    """
    if minutes > 0:
        for i in range(5, minutes, 5):

            calories_per_five_minutes = i * per_min

            print(f"{i:2d}:  {calories_per_five_minutes:>5,.1f}")

    total_calories = minutes * per_min

    print(f'{minutes}:  {total_calories:>5,.1f}')

    return


def open_triangle_print(rows):
    """
    -------------------------------------------------------
    Prints a triangle with an open center depending on the
    number of rows.
    Use: design = open_triangle_print(rows)
    -------------------------------------------------------
    Parameters:
        num_rows - number of rows of the triangle (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    height = rows

    blank_space = " "

    if height != 0:
        print("##")
    for i in range(1, height, 1):
        columns = i * blank_space
        print(f'#{columns}#')
    return


def mult_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: mult_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print("        ", end="")
    for i in range(start_num, stop_num + 1):
        print(f'{i}', end="    ")
    print()
    print("     ", end="")
    for j in range(start_num, stop_num + 1):
        print("-----", end="")
    print()

    for k in range(start_num, stop_num + 1):

        print(f'  {k} |', end="   ")

        for m in range(start_num, stop_num + 1):
            total = k * m
            if total < 10:
                print(total, end="    ")
            elif (total > 9) and (total < 100):
                print(total, end="   ")
            else:
                print(total, end="  ")
        print()

    return


def total_range(start_value, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum count values from start_value by increment.
    Use: sum_of_range = total_range(symbol, start_value, increment, count)
    -------------------------------------------------------
    Parameters:
        start_value - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        sum_of_range - the sum of the range (float)
    ------------------------------------------------------
    """
    total = 0

    for i in range(count):
        total += start_value
        start_value += increment

    return total
