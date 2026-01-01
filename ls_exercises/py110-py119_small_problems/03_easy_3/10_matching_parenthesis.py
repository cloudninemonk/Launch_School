'''
Write a function that takes a string as an argument and returns True if all parentheses in the string are properly balanced, False otherwise. To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

Note that balanced pairs must start with a (, not a ).

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True
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
- function return -> boolean
- program output -> boolean

Rules (Explicit):
- parentheses must occur in matching '(' and ')' pairs

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input:
- Output:

Example 2:
- Input:
- Output:

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
1.
2.
3.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

# I had significant difficulty in determining an algorithm for this one and hence, I looked at the solution after 30mins of trying to determine a solution.

# ==========
# LS Solution
# ==========

def is_balanced(s):
    parens = 0
    for char in s:
        if char == "(":
            parens += 1
        elif char == ")":
            parens -= 1
        if parens < 0:
            return False
    return parens == 0

