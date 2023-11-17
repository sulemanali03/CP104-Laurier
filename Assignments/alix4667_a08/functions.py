"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Suleman Ali
ID:      169044667
Email:   alix4667@mylaurier.ca
__updated__ = "2023-03-31"
-------------------------------------------------------
"""
# Imports

# Constants


def insert_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced_sentence = insert_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced_sentence - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced_sentence = ""

    for i in range(len(sentence)):
        if i > 0 and sentence[i].isupper():
            spaced_sentence += " "
        spaced_sentence += sentence[i]

    return spaced_sentence.capitalize()


def string_pluralizer(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized_string = string_pluralizer(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized_string - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    pluralized_string = string

    if string.endswith("s") or string.endswith("ch") or string.endswith("sh"):

        pluralized_string += "es"

    elif string.endswith("y") and not (string.endswith("oy") or string.endswith("ay")):

        pluralized_string = string.replace(string[-1], "ies")

    else:

        pluralized_string += "s"

    return pluralized_string


def common_postfix(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: postfix = common_postfix(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        postfix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    postfix = str2

    while not str1.endswith(postfix):
        postfix = postfix[1:]

    return postfix


def check_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = check_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """

    is_valid = True

    if len(isbn) != 17:
        is_valid = False
    elif not isbn[:3] in {'978', '979'}:
        is_valid = False
    elif not all(c.isdigit() or c == '-' for c in isbn):
        is_valid = False
    groups = isbn.split('-')
    if len(groups) != 5:
        is_valid = False
    for group in groups:
        if not group.isdigit():
            is_valid = False
    if not isbn[-1].isdigit():
        is_valid = False

    return is_valid


def check_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: is_word_chain = check_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a of strings (list of str, len > 1)
    Returns:
        is_word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    is_word_chain = True
    i = 0
    while i < len(words) - 1 and is_word_chain:
        if words[i][-1] != words[i+1][0]:
            is_word_chain = False
        i += 1
    return is_word_chain
