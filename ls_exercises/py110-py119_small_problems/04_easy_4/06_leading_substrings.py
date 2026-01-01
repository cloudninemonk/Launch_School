'''
Write a function that takes a string argument and returns a list of substrings of that string. Each substring should begin with the first letter of the word, and the list should be ordered from shortest to longest.

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
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
- list of substrings

Rules (Explicit):
- each substring should begin with the first letter of that word.

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

Edge Cases:
-

D: Data Structures
-------------------------
- range
- list


Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
Using a traditional loop
1. Pass the string argument to the leading_substrings function.
2. Initialise an empty string substring and initialise an empty list list_of_substrings
3. Loop through each character of the string and concatenate the current character to the substring
4. Append the substring to the list_of_substrings
5. Return the sorted list_of_substrings based on the length

Using a list comprehension
1. Pass the string argument to the leading_substrings function.
2. For each integer n from 0 up to and including the length of the string, take the substring slice from the first character to n + 1.
3. Collect these substrings in a list

Note: No need to sort the list as the strings are already in shortest to longest arrangement.

C: Code With Intent
-------------------------
"""
# using traditional loop

def leading_substrings(my_string):
    substring = ''
    list_of_substrings = []

    for char in my_string:
        substring += char
        list_of_substrings.append(substring)

    return list_of_substrings

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# using list comprehension

def leading_substrings(my_string):
    return [my_string[:idx + 1] for idx in range(len(my_string))]

print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# alternative list comprehension

def substring(s, idx):
    return s[:idx + 1]

def leading_substrings(my_string):
    return [substring(my_string, idx) for idx in range(len(my_string))]


print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])
