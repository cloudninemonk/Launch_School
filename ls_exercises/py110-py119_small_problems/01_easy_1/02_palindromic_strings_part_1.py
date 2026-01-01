'''
Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)
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
- boolean

Rules (Explicit):
- function must return a boolean
- case sensitive
- all characters matter

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input: 'madam'
- Output: True

Example 2:
- Input: '356653'
- Output: True

Example 3:
- Input: '356635'
- Output: False

Example 4:
- Input: 'Madam'
- Output: False

Example 4:
- Input: "madam i'm adam"
- Output: False

Edge Cases:
-

D: Data Structures
-------------------------
-

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string, original_string to the function is_palindrome
2. Assign the reverse of the string to a variable reversed_string
3. Return the boolean that results from checking if original_string is equal to reversed_string

C: Code With Intent
-------------------------
"""

# ==========
# My Solution
# ==========

def is_palindrome(original_string):
    '''Return True if original_string reads the same as the reverse of original_string'''
    return original_string[::-1] == original_string

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# ==========
# LS Solution
# ==========

def is_palindrome(s):
    return s == s[::-1]