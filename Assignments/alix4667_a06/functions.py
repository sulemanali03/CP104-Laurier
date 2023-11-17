"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-17"
-------------------------------------------------------
"""
# Imports
from random import randint
import ast
# Constants


def total_wins():
    """
    -------------------------------------------------------
    Returns how many times blue and grey teams won.
    Use: total_wins = winner()
    -------------------------------------------------------
    Parameters:
        none
    Returns:
        A tuple containing the number of times "blue" appeared in the input and the number
        of times "grey" appeared in the input
    -------------------------------------------------------
    """
    blue_wins = 0
    grey_wins = 0
    team = input("Enter the winning team: ")
    while team != "":
        if team.lower() == "blue":
            blue_wins += 1
        elif team.lower() == "grey":
            grey_wins += 1
        team = input("Enter the winning team: ")
    return blue_wins, grey_wins


def is_prime_number(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: is_prime = is_prime_number(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        is_prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    if number <= 1:
        is_prime = False
    else:
        is_prime = True
        i = 2
        while i * i <= number and is_prime:
            if number % i == 0:
                is_prime = False
            i += 1

    return is_prime


def interest_data(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_data(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    monthly_interest_rate = interest_rate / 1200

    balance = principal_amount
    month = 1

    print(f"Principal:   ${principal_amount:.2f}")
    print(f"Interest rate: {interest_rate:.2f}%")
    print(f"Monthly payment: ${payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while balance > 0:
        interest = balance * monthly_interest_rate
        balance += interest

        if balance < payment:
            payment = balance

        balance -= payment

        print(f"{month:4d} {interest:8.2f} {payment:8.2f} {balance:8.2f}")

        month += 1

    return


def count_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    num = abs(number)
    count = 0
    i = True
    while i is True:
        count += 1
        num = num // 10
        if num < 1:
            i = False

    return count


def sum_of_factors(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = sum_of_factors(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """
    total = 0
    factor = 1

    while number != 0 and factor < number:
        if number % factor == 0:
            total += factor
            factor += 1
        else:
            factor += 1
    return total
