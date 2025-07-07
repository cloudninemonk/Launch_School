"""
Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]
"""
# 1.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]

# 2.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list(reversed(numbers))

"""
LS Solution
"""
reversed_numbers = numbers[::-1]
reversed_numbers = list(reversed(numbers))
