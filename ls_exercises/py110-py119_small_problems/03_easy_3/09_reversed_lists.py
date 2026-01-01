'''
Write a function that takes a list as an argument and reverses its elements, in place. That is, mutate the list passed into the function. The returned object should be the same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list

Output:
- function return -> list
- program output -> boolean

Rules (Explicit):
- Cannot use reverse method
- Cannot use list slicing [::-1]

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

Edge Cases:
- Empty list

D: Data Structures
-------------------------
-

Notes
-------------------------
- for loop
- pop method
- insert method
- enumerate

A: Algorithm (Step-by-step)
-------------------------
1. Pass the list to the function reverse_list
2. Iterate over a range equal to the length - 1 of the list.
3. On each iteration remove the last element and insert it before the element at index of the current iteration count.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def reverse_list(lst):
    for n in range(len(lst) - 1): # Could omit the -1 in the range argument, however it would perform an extra iteration with no effect.
        lst.insert(n, lst.pop())
    return lst


list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

# ==========
# LS Solution
# ==========

# Solution 1

def reverse_list(lst):
    first = 0
    last = -1

    while first < (len(lst) // 2):
        lst[first], lst[last] = lst[last], lst[first]
        print(lst)
        first += 1
        last -= 1

    return lst

# Solution 2

def reverse_list(lst):
    n = len(lst)
    for idx in range(n // 2):
        lst[idx], lst[-(idx + 1)] = lst[-(idx + 1)], lst[idx]

    return lst