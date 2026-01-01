'''
Write a function that takes a string, doubles every consonant in the string, and returns the result as a new string. The function should not double vowels ('a','e','i','o','u'), digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included in the argument.

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")
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
- function return -> string
- program output -> boolean

Rules (Explicit):
- Only consonants to be doubled
- vowels, digits, punctuation, or whitespace not to be doubled
- Assume only ASCII characters will be in the argument string
- string can be empty

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

Edge Cases:
- strings can be empty and function should return an empty string

D: Data Structures
-------------------------
-

Notes
-------------------------
- generator
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Create a string CONSONANTS of consonants
2. Return the joining of each character multiplied by 2 if the character is in CONSONANTS, otherwise don't multiply the chararacter

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
def double_consonants(text):
    return ''.join(char * 2 if char.lower() in CONSONANTS else char for char in text)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# ==========
# LS Solution
# ==========

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(string):
    result = []

    for char in string:
        if char.lower() in CONSONANTS:
            result.append(char * 2)
        else:
            result.append(char)

    return ''.join(result)