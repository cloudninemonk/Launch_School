# 6. Is Empty?

"""
Write a function that checks whether a string is empty or not. For example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True
"""

# My response:

def is_empty(text):
    return text == ''               # Returns True if argument string is empty. Otherwise, False.

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

# LSBot comments:

"""
I was impressed by how cleanly you implemented this solution! There are a couple of alternative approaches worth considering:

You could use the len() function to check if the string has zero characters: return len(text) == 0

In Python, empty strings are "falsy," which means you could leverage this behavior: return not text

Both alternatives are equally valid solutions, and understanding these different approaches can deepen your knowledge of 
Python's behavior with strings. That said, your implementation is perfectly fine and demonstrates a clear understanding of 
the problem and how to solve it. You're on the right track with your Python learning!
"""
