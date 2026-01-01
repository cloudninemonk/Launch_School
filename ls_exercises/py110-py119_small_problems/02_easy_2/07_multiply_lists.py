'''
Write a function that takes two list arguments, each containing a list of numbers, and returns a new list that contains the product of each pair of numbers from the arguments that have the same index. You may assume that the arguments contain the same number of elements.

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- two lists

Output:
- function return -> list
- program output -> boolean

Rules (Explicit):
- lists contain numbers
- lists contain the same number of arguments

Rules (Implicit/Inferred):
- numbers are integers
- list are not empty

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- for loop
- zip function

A: Algorithm (Step-by-step)
-------------------------
1. Pass two lists, list1 and list2, to the function multiply_list.
2. Iterate through the zip of each list, multiplying the corresponding value1 and value2.
3. Append the resulting multiplication value to the list products.
4. Return products.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def multiply_list(list1, list2):
    products = []
    for value1, value2 in zip(list1, list2):
        products.append(value1 * value2)

    return products

# or

def multiply_list(list1, list2):
    products = []
    for idx in range(len(list1)):
        products.append(list1[idx] * list2[idx])

    return products

# or

def multiply_list(list1, list2):
    return [value1 * value2 for value1, value2 in zip(list1, list2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

# ==========
# LS Solution
# ==========

# Solution 1

def multiply_list(numbers1, numbers2):
    result = []

    for i in range(len(numbers1)):
        result.append(numbers1[i] * numbers2[i])

    return result

# Solution 2

def multiply_list(numbers1, numbers2):
    return [a * b for a, b in zip(numbers1, numbers2)]