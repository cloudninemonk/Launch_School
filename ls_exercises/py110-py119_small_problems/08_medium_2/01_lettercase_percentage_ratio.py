'''
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string

Output:
- dictionary

Rules (Explicit):
- dictionary keys and values to be strings
- values to be numbers with two decimal places
-

Rules (Implicit/Inferred):
- all characters are to be considered, including whitespace.
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

Edge Cases:
-

D: Data Structures
-------------------------
- dictionary comprehension

Notes
-------------------------
- for loop in comprehension
- need to determine how to get two decimal places of a float

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string argument to the function letter_percentages
2. Determine the length of the argument and assign it to str_len
3. Initialise a dictionary with three keys, 'lowercase', 'uppercase', 'neither' and pair with a value of 0 for each.
3. Initialise three variables, lowercase_count, uppercase_count, neither_count to 0.
4. Iterate through the string argument one character at a time and check if character is lower, upper or neither. Increase count of the respective variable.
5. At the end of iterating, determine the float percentage of lowercase_count, uppercase_count and neither_count and update the dictionary with those percentages to decimal places and convert to a string.
6. Return the dictionary



C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def percentage_calc(count, string_length):
    return f"{count / string_length * 100:.2f}"

def letter_percentages(string):
    str_len = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0

    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1

    return {
        'lowercase':percentage_calc(lowercase_count, str_len),
        'uppercase':percentage_calc(uppercase_count, str_len),
        'neither_case':percentage_calc(neither_count, str_len)
    }

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

# ==========
# LS Solution
# ==========



