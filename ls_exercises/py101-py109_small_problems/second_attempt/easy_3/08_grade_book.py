"""
Write a function that determines the mean (average) of the three scores passed
to it, and returns the letter associated with that grade.

Numerical score letter grade list:

90 <= score <= 100: 'A'
80 <= score < 90: 'B'
70 <= score < 80: 'C'
60 <= score < 70: 'D'

0 <= score < 60: 'F'

Tested values are all between 0 and 100. There is no need to check for negative
values or values greater than 100.

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- 3 x integers

Output:
- a single character string

Rules (Explicit):
- Function to take three numerical scores
- Calculates the average
- Returns the corresponding letter grade

Rules (Implicit/Inferred):
- Scores assumed to be integers between 0 and 100, inclusive.
- Assume inputs are valid

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input: 95, 90, 93
- Output: "A"

Example 2:
- Input: 50, 50, 95
- Output: "D"

Edge Cases:
-

D: Data Structures
-------------------------
- lists

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. 3 numerical scores passed to the function
2. Calculate the average and assign to a variable
3. Pass the average grade to a helper function that matches the case
4. Return the case that matches to the parent function
5. Return the letter grade to the invoking print statement

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def get_grade(num1, num2, num3):
    avg_grade = (num1 + num2 + num3) / 3
    return get_letter_grade(avg_grade)

def get_letter_grade(avg_grade):
    match avg_grade:
        case _ if avg_grade >= 90:
            return 'A'
        case _ if avg_grade >= 80:
            return 'B'
        case _ if avg_grade >= 70:
            return 'C'
        case _ if avg_grade >= 60:
            return 'D'
        case _ if avg_grade < 60:
            return 'F'

print(get_grade(95, 90, 93) == "A")
print(get_grade(50, 50, 95) == "D")


