"""
Write a function that takes one argument, a positive integer, and returns a
string of alternating '1's and '0's, always starting with a '1'. The length of
the string should match the given integer.

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- positive integer

Output:
- string of numbers

Rules (Explicit):
- output to begin with '1'
- length of string to equal integer

Rules (Implicit/Inferred):
- Cannot have an empty argument

Mental Model (Optional):
-


E: Examples / Test Cases
-------------------------
Example 1:
- Input: 6
- Output: '101010'

Example 2:
- Input: 1
- Output: '1'

Edge Cases:
- Input: '0'
- Output: ''


D: Data Structures
-------------------------
- strings

Notes:
- loops, for loop
-



A: Algorithm (Step-by-step)
-------------------------
1. Function receives an integer argument
2. Initialise an empty string to store the output
3. Loop through the range of the integer
4. For each iteration, determine whether the element of the range modulo 2 is zero or not.
5. If modulo does equal zero, augment the output string to add '1'
6. If modulo does not equal zero, augment the output string to add '0'
7. Return string at the end of loop



C: Code With Intent
-------------------------
"""

# ==========
# My Solution
# ==========

def stringy(integer):
    result = ''
    for i in range(integer): # i: 0
        if i % 2 == 0:
            result += '1'    # result: '1'
        else:
            result += '0'

    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True