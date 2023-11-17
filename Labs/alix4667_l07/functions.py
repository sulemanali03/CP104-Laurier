"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-28"
-------------------------------------------------------
"""
# Imports
from random import randint
# Constants


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)

    guess = int(input("Guess:"))

    count = 0

    while guess != number:

        if guess > number:
            print("Too high, try again.")

        elif guess < number:
            print("Too low, try again.")

        guess = int(input("Guess: "))

        count = count + 1

    count = count + 1
    print("Congratulations - good guess!")

    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """

    power = 1
    while power < target:
        power *= 2
    return power


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """

    n = 1
    sum_of_squares = 1
    while sum_of_squares < target:
        n += 1
        sum_of_squares += n*n

    final = 0
    for i in range(1, n+1):
        final += i*i

    return final


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0

    day = 1
    another_day = True

    while another_day:
        print(f"For Day {day}\n")
        b_cost = float(input("How much was breakfast? $"))
        l_cost = float(input("How much was lunch? $"))
        s_cost = float(input("How much was supper? $"))

        meals_total = b_cost + l_cost + s_cost
        a_total += meals_total
        b_total += b_cost
        l_total += l_cost
        s_total += s_cost

        print(f"Your total for the day was ${meals_total:.2f}\n")
        day += 1
        response = input("Were you away another day (Y/N)? ")
        if response != "Y":
            another_day = False

    return b_total, l_total, s_total, a_total


TAX_RATE = 0.03625
OVERTIME_RATE = 1.5
MAX_REGULAR_HOURS = 40


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    total_wages = 0
    count = 0
    employee_id = input("Employee ID: ")

    while employee_id != "0":
        wage_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))

        if hours_worked <= MAX_REGULAR_HOURS:
            gross_wages = wage_rate * hours_worked
        else:
            regular_wages = wage_rate * MAX_REGULAR_HOURS
            overtime_wages = (hours_worked - MAX_REGULAR_HOURS) * \
                wage_rate * OVERTIME_RATE
            gross_wages = regular_wages + overtime_wages

        net_wages = gross_wages * (1 - TAX_RATE)
        total_wages += net_wages
        count += 1
        print(f"Net payment for employee {employee_id}: ${net_wages:.2f}\n")

        employee_id = input("Employee ID: ")

    average_wages = total_wages / count if count != 0 else 0
    return total_wages, average_wages
