"""
Write a function that takes a positive integer, n, as an argument and prints a
right triangle whose sides each have n stars. The hypotenuse of the triangle
(the diagonal side in the images below) should have one end at the lower-left of
the triangle, and the other end at the upper-right.

Examples:
triangle(5)

Output:
    *
   **
  ***
 ****
*****
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- positive integer, n

Output:
- A string of spaces and stars

Rules (Explicit):
- Each side of the triangle should have n stars
- Hypotentus runs from top right to bottom left

Rules (Implicit/Inferred):
- Non-hypotenuse sides of the triangle to be on the right and the bottom
- The stars are strings
- Output to be included in the function

Mental Model (Optional):
-


E: Examples / Test Cases
-------------------------
Example 1:
- Input: 5
- Output:
    *
   **
  ***
 ****
*****

Edge Cases:
- 0, 1, -1


D: Data Structures
-------------------------
- strings

Notes
-------------------------
- loop, for loop

A: Algorithm (Step-by-step)
-------------------------
1. Function receives positive integer argument, n
2. Iterate through integers 1 to n, inclusive
3. print (n - current iteration) number of spaces followed by,
   current iteration number of stars

C: Code With Intent
-------------------------
"""

def triangle(integer):

    for i in range(1, integer + 1):
        print(f"{(integer - i) * ' '}{i * '*'}")

triangle(5)
triangle(0)
triangle(10)