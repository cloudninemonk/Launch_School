"""
Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]
"""
# 1.
numbers = [1, 2, 3, 4]
numbers.clear()

# 2.
numbers = [1, 2, 3, 4]
while numbers:
    numbers.remove(numbers[0])

# ==========
# LS Solution
# ==========

# Approach 1
numbers.clear()

#Approach 2
while numbers:
   numbers.pop()

# Note that the following solution will set numbers to an empty list, but it
# doesn't clear the original list. That's fine if you know there are no other
# references to the list.

# numbers = []

# ==========
# Comments
# ==========

# | Method               | Removes from | Performance | Preferred when                                       |
# | -------------------- | ------------ | ----------- | ---------------------------------------------------- |
# | `remove(numbers[0])` | Front (left) | O(n)        | Rarely (inefficient)                                 |
# | `pop()`              | End (right)  | O(1)        | ✅ When order doesn’t matter or LIFO (stack behavior) |
# | `pop(0)`             | Front (left) | O(n)        | ❌ Avoid for large lists unless necessary             |
