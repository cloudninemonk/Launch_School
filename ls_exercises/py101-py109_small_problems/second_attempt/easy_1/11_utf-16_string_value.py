"""
Write a function that determines and returns the UTF-16 string value of a string
passed in as an argument. The UTF-16 string value is the sum of the UTF-16
values of every character in the string. (You may use ord to determine the
UTF-16 value of a character.)

# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
"""
# ==========
# My Solution
# ==========

def utf16_value(string):
    result = 0
    for char in string:
        result += ord(char)
    return result

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)

OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# ==========
# LS Solution
# ==========

def utf16_value(string):
    sum_ = 0
    for char in string:
        sum_ += ord(char)
    return sum_

# Discussion
# The solution starts by initializing a variable sum_ to 0.

# We named the variable sum_ (with an underscore suffix) to avoid shadowing
# Python's built-in sum function. Overriding or shadowing built-in names can
# lead to confusion and unexpected behavior.

# The function iterates through each character in the given string using a for
# loop. For each character, we use the ord function to get its UTF-16 value and
# add it to the sum. Finally, after iterating through all characters, the
# function returns the sum of all the character values.

# Python's built-in ord function returns the Unicode code point for a string of
# one character. In the context of this problem, it gives us the UTF-16 value
# for each character, which lets us calculate the desired sum.