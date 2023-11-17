"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-03"
-------------------------------------------------------
"""
# Imports

# Constants


def day_of_the_week(day_number):
    """
    -------------------------------------------------------
    Returns the day of the week depending on the user integer.
    1 = Sunday
    2 = Monday
    3 = Tuesday
    4 = Wednesday
    5 = Thursday
    6 = Friday
    7 = Saturday
    Returns "Error" if number is less than 1 or greater than 7
    Use: day = day_of_the_week(day_number)
    -------------------------------------------------------
    Parameters:
        day_number - an integer (int > 0)
    Returns:
        day - the day of the week (str)
    ------------------------------------------------------
    """
    # Constants
    DAY_ONE = 'Sunday'
    DAY_TWO = 'Monday'
    DAY_THREE = 'Tuesday'
    DAY_FOUR = 'Wednesday'
    DAY_FIVE = 'Thursday'
    DAY_SIX = 'Friday'
    DAY_SEVEN = 'Saturday'

    if (day_number < 1) or (day_number > 7):
        day = "Error"
    elif day_number == 1:
        day = DAY_ONE
    elif day_number == 2:
        day = DAY_TWO
    elif day_number == 3:
        day = DAY_THREE
    elif day_number == 4:
        day = DAY_FOUR
    elif day_number == 5:
        day = DAY_FIVE
    elif day_number == 6:
        day = DAY_SIX
    else:
        day = DAY_SEVEN
    return day


def level_of_pollution(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if aqi is negative.
    Use: level_of_pollution(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        level - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index < 0:
        level = "Error"
    elif 0 <= air_quality_index <= 50:
        level = "Good"
    elif 51 <= air_quality_index <= 100:
        level = "Moderate"
    elif 101 <= air_quality_index <= 150:
        level = "Unhealthy for Sensitive Groups"
    elif 151 <= air_quality_index <= 200:
        level = "Unhealthy"
    elif 201 <= air_quality_index <= 300:
        level = "Very Unhealthy"
    else:
        level = "Hazardous"

    return level


def largest_product(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the product of the two largest values of
    val1, val2, and val3.
    Use: product = largest_product(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        product - the product of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    product = 0
    if val1 >= val2:
        if val3 >= val2:
            product = int(val1 * val3)
        else:
            product = int(val1 * val2)
    elif val2 >= val1:
        if val3 >= val1:
            product = int(val2 * val3)
        else:
            product = int(val2 * val1)

    return product


def colour_mix(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_mix(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if (rgb_colour1 == "red" and rgb_colour2 == "blue") or (rgb_colour2 == "red" and rgb_colour1 == "blue"):
        colour = "fuchsia"
    elif (rgb_colour1 == "red" and rgb_colour2 == "green") or (rgb_colour2 == "red" and rgb_colour1 == "green"):
        colour = "yellow"
    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        colour = "red"
    elif (rgb_colour1 == "green" and rgb_colour2 == "blue") or (rgb_colour2 == "green" and rgb_colour1 == "blue"):
        colour = "aqua"
    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        colour = "green"
    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        colour = "blue"
    else:
        colour = "Error"

    return colour


def yee_ha(number):
    """
    -------------------------------------------------------
    Determines if program is divisible by 3, or 7, or both.
    Returns "Yee" if number is evenly divisible by 3, "Ha"
    if number is evenly divisible by 7, "Yee Ha" if number
    is evenly divisible by both 3, and 7, and "Nada" if
    number is none of the above.
    Use: result = yee_ha(number)
    -------------------------------------------------------
    Parameters:
        number - an integer
    Returns:
        result = the result of the quotient
    ------------------------------------------------------
    """
    # Constants
    YEE = "Yee"
    HA = "Ha"
    YEE_HA = "Yee Ha"
    NADA = "Nada"

    remainder_one = number % 3
    remainder_two = number % 7

    if remainder_one == 0 and remainder_two == 0:
        result = YEE_HA
    elif remainder_one == 0:
        result = YEE
    elif remainder_two == 0:
        result = HA
    else:
        result = NADA
    return result
