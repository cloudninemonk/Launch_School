'''
Write a function that takes a list of positive integers as input, multiplies all of the integers together, divides the result by the number of entries in the list, and returns the result as a string with the value rounded to three decimal places.

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list

Output:
- function return -> string
- program output -> boolean

Rules (Explicit):
- input list contains positive integers
- function return is a float string
- string value rounded to three decimal places

Rules (Implicit/Inferred):
- input list to contain at least 2 elements
- input list elements are integers

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")

Edge Cases:
-

D: Data Structures
-------------------------
- str

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the list to the function multiplicative_average
2. Initialise the variable value to the first element of the input list.
3. Iterate through the list from the next to first element, inclusive.
4. On each iteration, update value by multiplying it by the value in the input list at the current iteration.
5. Once iteration has completed, divide the value by the length of the input list and round to 3 decimal places.
6. Return the string of the value.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def multiplicative_average(lst):
    product = 1
    try:
        for value in lst:
            product *= value

        return f'{product / len(lst):.3f}'
    except ZeroDivisionError:
        print('The input list is empty and hence you cannot divide by zero')



# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
print(multiplicative_average([]) == "28361.667")

# ==========
# LS Solution
# ==========
def round_to_three_digits(number):
    rounded_number_as_str = str(round(number, 3))
    decimal_position = rounded_number_as_str.find('.')

    while len(rounded_number_as_str) - decimal_position < 4:
        rounded_number_as_str += '0'

    return rounded_number_as_str

def multiplicative_average(numbers):
    product = 1

    for num in numbers:
        product *= num

    return round_to_three_digits(product / len(numbers))

# Solution 2

def round_to_three_digits(number):
    return f"{number:.3f}"

def multiplicative_average(numbers):
    product = 1

    for num in numbers:
        product *= num

    return round_to_three_digits(product / len(numbers))