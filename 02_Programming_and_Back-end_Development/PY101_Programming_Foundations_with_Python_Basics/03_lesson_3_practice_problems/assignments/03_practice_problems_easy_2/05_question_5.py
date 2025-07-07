"""
How would you verify whether the data structures assigned to the variables
numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}
"""

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)

# ==========
# LS Solution
# ==========

# Preferred solution

isinstance(numbers, list)  # True
isinstance(table, list)    # False


# this works too, but has potential issues
type(numbers) is list      # True
type(table) is list        # False

# ==========
# ChatGPT Explanation
# ==========

# 💡 Why `isinstance()` is better:
#
# ✅ Works even if the object is an instance of a subclass of `list`
# ✅ Cleaner, more Pythonic
# ❌ `type(x) is list` fails for subclasses (e.g., custom list types)





