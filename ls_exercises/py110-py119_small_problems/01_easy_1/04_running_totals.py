'''
Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list of integers

Output:
- boolean

Rules (Explicit):
- function to return a list of integers

Rules (Implicit/Inferred):
- elements are integers

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- for loop
- append method
- integer concatentation

A: Algorithm (Step-by-step)
-------------------------
1. Invoke function running_total with the list original_numbers of integers as the argument.
2. Initialise totals_list as an empty list
3. Initialise current_value to 0
4. Iterate through each element of the original list and concatenate the value to current_value
5. Append the current_value to running_total
6. Return the totals_list

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def running_total(original_numbers):
    totals_list = []
    current_value = 0
    for number in original_numbers:
        current_value += number
        totals_list.append(current_value)

    return totals_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

# ==========
# LS Solution
# ==========

def running_total(nums):
    result_list = []
    total = 0

    for num in nums:
        total += num
        result_list.append(total)

    return result_list
