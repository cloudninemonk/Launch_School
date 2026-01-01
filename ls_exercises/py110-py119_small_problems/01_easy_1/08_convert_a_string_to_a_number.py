'''
Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string of digits

Output:
- boolean

Rules (Explicit):
- all characters are numeric
- cannot use standard conversion functions such as int
- ignore + or - signs
- ignore invalid characters

Rules (Implicit/Inferred):
- numbers are integers

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True.

Edge Cases:
-

D: Data Structures
-------------------------
- dictionary to contain integers 0 to 9 to look up

Notes
-------------------------
- function to return an integer

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string to the function string_to_integer.
2. Create a dictionary DIGITS of digits 0 to 9 values assigned to respective keys '0' to '9'.
3. Determine the len of the string and assign to string_len.
4. Initialise a variable value to 0. This will be updated and returned with the final integer.
4. Iterate through each character within the string and obtain the respective index.
5. Update value with the value assigned to the digit string in DIGITs and multiply by 10^(string_len - 1).
7. Return the final value after looping.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def string_to_integer(string_of_digits):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    string_len = len(string_of_digits)
    value = 0

    for idx, char in enumerate(string_of_digits):
        value = value + DIGITS[char] * 10**(string_len - idx - 1)

    return value

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

# ==========
# LS Solution
# ==========

def string_to_integer(s):
    DIGITS = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    value = 0
    for char in s:
        value = (10 * value) + DIGITS[char]
        print(value)

    return value

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True