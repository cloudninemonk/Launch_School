"""
A double number is an even-length number whose left-side digits are exactly the
same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all
double numbers, whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument multiplied by
two, unless the argument is a double number. If the argument is a double number,
return the double number as-is.

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integer

Output:
- input * 2 or input pending meeting the condition

Rules (Explicit):
- multiply input integer by 2 unless it is a double number

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input: 37 # not a double number
- Output: 74

Example 2:
- Input: 44 # is a double number
- Output: 44

Edge Cases:
- odd length numbers

D: Data Structures
-------------------------
- strings

Notes
-------------------------
- len function
- if/else statements

A: Algorithm (Step-by-step)
-------------------------
1. Integer is passed to the function
2. Determine if the number is odd in length and return number * 2 if it is.
3. If not odd, determine if the slice of the left half == the slice of the right half.
4. If both halves are equal, return the number as is
5. If both halves are not equal, return the number * 2

C: Code With Intent
-------------------------
"""
def twice(integer):
    integer_string = str(integer)
    middle_of_string = len(integer_string) // 2

    if integer_string[:middle_of_string] == integer_string[middle_of_string:]:
        return integer
    else:
        return integer * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True