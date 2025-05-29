# 7. Is Empty or Blank?

"""
Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. 
For example:

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True
"""

# My response:

def is_empty_or_blank(s):
    return not s.strip() # Returns True if the string is empty or only contains whitespace.

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True