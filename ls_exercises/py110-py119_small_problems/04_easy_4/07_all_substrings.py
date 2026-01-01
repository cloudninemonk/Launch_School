'''
Write a function that returns a list of all substrings of a string. Order the returned list by where in the string the substring begins. This means that all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on. Since multiple substrings will occur at each position, return the substrings at a given index from shortest to longest.

You may (and should) use the leading_substrings function you wrote in the previous exercise:

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True
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
- list of strings which are substrings of the input string

Rules (Explicit):
- Use the function from the previous exercise.
- Order the returned list by where in the string the substring begins. i.e., all substrings that start at index position 0 should come first, then all substrings that start at index position 1, and so on.

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- list comprehension
- nested for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string argument to the substrings function.
2. For each integer n from 0 to length of the string argument, take the substring slice from the first character to n + 1.
3. Repeat step 2 starting from n + 1.
4. Collect these substrings in a list.

Note: No need to sort the list as already sorted in lexicographical when building the list.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def substrings(my_string):
    return [my_string[idx:idx2 + 1] for idx in range(len(my_string)) for idx2 in range(idx, len(my_string))]

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# alternative solution

def leading_substrings(my_string):
    return [my_string[:idx + 1] for idx in range(len(my_string))]

def substrings(my_string):
        return [substring for idx in range(len(my_string)) for substring in leading_substrings(my_string[idx:])]

# idx = 0
# my_string[0:] = 'abcde'
# leading_substrings returns ['a', 'ab', 'abc', 'abcd', 'abcde']
# substrings then iterates through the return list and adds each element to it's own list
# substrings list when idx = 0: ['a', 'ab', 'abc', 'abcd', 'abcde']

# idx = 1
# my_string[1:] = 'bcde'\
# leading_substrings returns ['b', 'bc', 'bcd', 'bcde']
# substrings then iterates through the return list and adds each element to it's own list
# substrings list when idx = 1: ['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'bc', 'bcd', 'bcde']

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# ==========
# LS Solution
# ==========

# solution 1
def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    results = []
    for idx in range(len(string)):
        string_at_idx = string[idx:]
        for substring in leading_substrings(string_at_idx):
            results.append(substring)

    return results

# solution 2

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    return [
        substring
        for idx in range(len(string))
        for substring in leading_substrings(string[idx:])
    ]


