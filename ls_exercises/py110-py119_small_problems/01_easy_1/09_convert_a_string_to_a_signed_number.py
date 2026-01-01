'''
In the previous exercise, you developed a function that converts simple numeric strings to integers. In this exercise, you're going to extend that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate number as an integer. The string may have a leading + or - sign; if the first character is a +, your function should return a positive number; if it is a -, your function should return a negative number. If there is no sign, return a positive number.

You may assume the string will always contain a valid number.

You may not use any of the standard conversion functions available in Python, such as int. You may, however, use the string_to_integer function from the previous exercise.

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True
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
- number should be negative if - is present i.e. '-101' should be -101
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
- absolute function

Notes
-------------------------
- function to return an integer
-

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string to the function string_to_signed_integer.
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
def string_to_signed_integer(text):
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

    sign = -1 if text[0] == '-' else 1
    start = 1 if text[0] in '+-' else 0

    value = 0
    for char in text[start:]:
        value = (value * 10) + DIGITS[char]

    return sign * value

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

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

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)