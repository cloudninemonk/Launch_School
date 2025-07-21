"""
Write a function that takes two strings as arguments, determines the length of the
two strings, and then returns the result of concatenating the shorter string,
the longer string, and the shorter string once again. You may assume that the
strings are of different lengths.
"""

def short_long_short(string1, string2):
    """Concatenate the strings according to: shortest string + longest string
    + shortest string"""
    if len(string1) < len(string2):
        return string1 + string2 + string1
    return string2 + string1 + string2

get_string1 = input("Enter a string: ")
get_string2 = input("Enter another string: ")

print(short_long_short(get_string1, get_string2))
