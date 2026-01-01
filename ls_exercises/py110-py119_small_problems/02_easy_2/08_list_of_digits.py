'''
Write a function that takes one argument, a positive integer, and returns a list of the digits in the number.

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True
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
- list of integers

Rules (Explicit):
- input integer is positive

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

Edge Cases:
-

D: Data Structures
-------------------------
- str
- list

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the integer to the function digit_list
2. Convert the integer to a string number
3. Iterate throught the string and append the element on each iteration to the list digits
4. Return digits

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def digit_list(number):
    return [int(char) for char in str(number)]

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True

# ==========
# LS Solution
# ==========

def digit_list(number):
    return [int(digit) for digit in str(number)]