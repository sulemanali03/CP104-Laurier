"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-05-09"
-------------------------------------------------------
"""
# Imports

# Constants


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """

    if day * month == year:
        magic = True
    else:
        magic = False
    return magic


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    v1_target_diff = abs(target-v1)
    v2_target_diff = abs(target-v2)

    if v1_target_diff > v2_target_diff:
        result = v2
    else:
        result = v1
    return result


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """

    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        numeral = None
    return numeral


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time greater than or equal to 10 years service
        1.5% for full time less than 4 years service
        3% for part time greater than 10 years service
        1% for part time less than 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """

    RAISE1 = 0.05
    RAISE2 = 0.015
    RAISE3 = 0.03
    RAISE4 = 0.01
    RAISE5 = 0.02

    if status == "F" and years >= 10:
        new_salary = salary+(salary * RAISE1)
    elif status == "F" and years < 4:
        new_salary = salary+(salary * RAISE2)
    elif status == "P" and years > 10:
        new_salary = salary+(salary * RAISE3)
    elif status == "P" and years < 4:
        new_salary = salary+(salary * RAISE4)
    else:
        new_salary = salary+(salary * RAISE5)
    return new_salary


# Constants
INFANT = 0.00
SENIOR = 4.00
STUDENT = 3.00
STUDENT_OF_SCHOOL = 1.00
ADULT = 5.00
KID = 2.00
INFANT_AGE = 3
SENIOR_AGE = 65
STUDENT_AGE1 = 10
STUDENT_AGE2 = 18
ADULT_AGE1 = 18
ADULT_AGE2 = 65


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age < 3): $0
        Senior (age >= 65): $4.00
        Student (10 <= age < 18): $3.00
            Student of this school: $1.00
        Adult (18 <= age < 65): $5.00
        Kid (3 <= age < 10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """

    age = int(input("How old are you?"))
    if age < INFANT_AGE:
        price = INFANT
    elif age >= SENIOR_AGE:
        price = SENIOR
    elif ADULT_AGE1 <= age < ADULT_AGE2:
        price = ADULT
    elif STUDENT_AGE1 <= age < STUDENT_AGE2:
        school = input("Are you a student at this school?: ")
        if school == "Y":
            price = STUDENT_OF_SCHOOL
        else:
            price = STUDENT
    else:
        price = KID
    return price
