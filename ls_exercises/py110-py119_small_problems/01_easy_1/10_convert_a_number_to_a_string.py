'''
In the previous two exercises, you developed functions that convert simple numeric strings to signed integers. In this exercise and the next, you're going to reverse those functions.

Write a function that converts a non-negative integer value (e.g., 0, 1, 2, 3, and so on) to the string representation of that integer.

You may not use any of the standard conversion functions available in Python, such as str. Your function should do this the old-fashioned way and construct the string by analyzing and manipulating the number.

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integer

Output:
- function return: string
- program output: boolean

Rules (Explicit):
- Cannot use string function

Rules (Implicit/Inferred):
- function argument is an integer


Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

Edge Cases:
-

D: Data Structures
-------------------------
- string
- list

Notes
-------------------------
- while loop
- divmod function

A: Algorithm (Step-by-step)
-------------------------
1. Create a constant variable DIGITS for the integer keys 0 to 9 with '0' to '9' as the respective values
2. Pass the argument to the function integer_to_string
3. Create an empty list digits
4. Divide the number passed to the function by 10 and determine the remainder. Hint: Use divmod function
5. Use the remainder as an index to extract the string integer from DIGITS and append it to the list digits.
6. Repeat steps 4 and 5 until the last digit.
7. After iterating, return the digit_string.


C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
DIGITS = '0123456789'

def integer_to_string(number):
    digits= []

    while number > 0:
        number, remainder = divmod(number, 10)
        digits.append(DIGITS[remainder])
        if number == 0:
            break
    digits.reverse()
    return ''.join(digits)

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True

# ==========
# LS Solution
# ==========

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'