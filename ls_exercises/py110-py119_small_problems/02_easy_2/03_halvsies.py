'''
Write a function that takes a list as an argument and returns a list that contains two elements, both of which are lists. Put the first half of the original list elements in the first element of the return value and put the second half in the second element. If the original list contains an odd number of elements, place the middle element in the first half list.

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
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
- function return value -> list of lists
- program output -> boolean

Rules (Explicit):
- Returned list to contain two elements which are lists.
- First half of elements in the input list go into the first element list of the returned list and the second half to the second element list.
- For odd number of elements in the input list, the middle element to go into the first list.

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

Edge Cases:
- Empty input list to return a list of two empty list elements.

D: Data Structures
-------------------------
- list

Notes
-------------------------
- for loop

A: Algorithm (Step-by-step)
-------------------------
1. Pass the list to the function halvies
2. Determine whether the length of the list is odd or even
3. Initialise two empty lists, list1 and list2
4. If length of list is odd, iterate through all elements of the input list from start to the middle, inclusive, and add the elements to list1. Iterate through all elements of the input list from the first element after the middle one to the end, inclusive and assign to list2.
5. If length of list is even, iterate through the first half of the input list and add elements to list1. Iterate through the second half of the input list and add elements to list2.
6. Return a list of list1 and list2 as element 0 and element 1, respectively.


C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def halvsies(lst):
    list1 = []
    list2 = []

    if not lst:
        return [[], []]
    elif len(lst) % 2 == 0:
        list1.extend(lst[:len(lst) // 2])
        list2.extend(lst[len(lst) // 2:])
    else:
        list1.extend(lst[:len(lst) // 2 + 1])
        list2.extend(lst[len(lst) // 2 + 1:])

    return [list1, list2]

# LSBot provided solution

def halvsies(lst):
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

# Comments:
# The difference between my solution and the LSBot provided solution is that the bot determined a single way ((len(lst) + 1) // 2) to determine the mid-point of the list that can be implemented in the list slice. Whereas, I implemented one way for odd (len(lst) // 2 + 1) and another for even (len(lst) // 2).

# ==========
# LS Solution
# ==========

def halvsies(lst):
    half = (len(lst) + 1) // 2
    first_half = lst[:half]
    second_half = lst[half:]
    return [first_half, second_half]


