"""
Given a string that consists of some words and an assortment of non-alphabetic
characters, write a function that returns that string with all of the
non-alphabetic characters replaced by spaces. If one or more non-alphabetic
characters occur in a row, you should only have one space in the result (i.e.,
the result string should never have consecutive spaces).

print(clean_up("---what's my +*& line?") == " what s my line ")
# True
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input: - string inc. non-alphabetical characters

Output: - string

Rules (Explicit): - replace non-alphabetical characters with spaces - maximum of
one space for any sequence of non-alphabetical characters

Rules (Implicit/Inferred): -

Mental Model (Optional): -

E: Examples / Test Cases
-------------------------
Example 1: - Input: "---what's my +*& line?" - Output: " what s my line "

Edge Cases: -

D: Data Structures
-------------------------
- string
- list
- range

Notes
-------------------------
- if/else statement
- append function
- len function
- isalpha() function
- loop, for loop
- enumerate

A: Algorithm (Step-by-step)
-------------------------
1. define a function that accepts a string argument -> parameter,
   original_string
2. assign an empty string to the variable new_string
3. iterate through the original_string character by character
4. check if original_string[i] isalpha and if index is 0. If so, augment
   new_string by adding a space
5. elif: original_string[i] is not alpha and original_string[i-1] is alpha,
   augment new_string with ' '
6. elif: original_string[i] is alpha, augment new_string with original_string[i]
7. else: continue

C: Code With Intent
-------------------------
"""

# ==========
# My Solution
# ==========

def clean_up(original_string):
    new_string = []
    for idx, char in enumerate(original_string):
        if (
            not char.isalpha() and (idx == 0
            or original_string[idx - 1].isalpha())
        ):
            new_string.append(' ')
        if char.isalpha():
            new_string.append(char)

    return ''.join(new_string)

print(clean_up("---what's my +*& line?") == " what s my line ")