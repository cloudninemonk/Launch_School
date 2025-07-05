# 8. Matrix

"""
We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. 
However, we encountered an issue, as whenever we change a value in one nested list, 
all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
"""

# My response:
"""
matrix.append(sub_list) result in a shallow copy of sub_list being performed
on each iteration. Therefore, a change to one nested list results in the change
to all corresponding elements in the other nested lists. 

The following includes a deep copy to avoid shallow copying from occurring.
"""

import copy 

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# LSBot's comments:

"""
Opportunities for improvement
I was impressed by your understanding of deep copying concepts! While your solution 
with deepcopy works perfectly, I'd like to point out that for simple lists like this 
one, using sub_list.copy() or list(sub_list) would also be sufficient since we're 
only dealing with immutable objects (strings) within the lists. The deepcopy function 
is more resource-intensive and is typically needed when dealing with nested mutable 
objects. That said, your solution is absolutely correct and shows you're thinking 
ahead about more complex data structures.

As you continue with Python, being aware of when to use shallow vs. deep copying will 
serve you well for more complex data structures. Great job on this exercise!
"""