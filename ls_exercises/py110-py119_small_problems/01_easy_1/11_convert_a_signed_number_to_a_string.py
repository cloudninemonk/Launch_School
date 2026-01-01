'''
In the previous exercise, you developed a function that converts non-negative numbers to strings. In this exercise, you're going to extend that function by adding the ability to represent negative numbers as well.

Write a function that takes an integer and converts it to a string representation.

You may not use any of the standard conversion functions available in Python, such as str. You may, however, use integer_to_string from the previous exercise.

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- signed or non-signed integer

Output:
- function return value is a string
- program output is a boolean

Rules (Explicit):
- cannot use the str or int functions

Rules (Implicit/Inferred):
- can use list constructor

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

Edge Cases:
-

D: Data Structures
-------------------------
- list constructor

Notes
-------------------------
- divmod function
- while loop
- abs function

A: Algorithm (Step-by-step)
-------------------------
Note: This program relies on the function integer_to_string created in the program in the previous exercise.
1. Create a constant variable DIGITS for the integer keys 0 to 9 with '0' to '9' as the respective values
2. Pass the argument to the function signed_integer_to_string
3. Create three if conditions based on whether number is 0, > 0 or < 0.
4. If 0, return '0'
5. If > 0, return +integer_to_string(number)
6. If < 0, return -integer_to_string(abs(number))
4. Divide the number passed to the function by 10 and determine the remainder. Hint: Use divmod function
5. Use the remainder as an index to extract the string integer from DIGITS and append it to the list digits.
6. Repeat steps 4 and 5 until the last digit.
7. After iterating, return the digit_string.

C: Code With Intent
-------------------------
"""
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def integer_to_string(number):
    digits= []

    while number > 0:
        number, remainder = divmod(number, 10)
        digits.append(DIGITS[remainder])
        if number == 0:
            break
    digits.reverse()
    return ''.join(digits)

def signed_integer_to_string(number):
    if number == 0:
        return '0'
    elif number < 0:
        return f'-{integer_to_string(abs(number))}'
    else:
        return f'+{integer_to_string(abs(number))}'

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True

# ==========
# LS Solution
# ==========

def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"