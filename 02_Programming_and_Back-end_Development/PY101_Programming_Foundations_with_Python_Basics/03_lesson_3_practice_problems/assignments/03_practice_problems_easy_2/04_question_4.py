"""
Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the number
at index 2, so that the list becomes [1, 2, 4, 5].
"""

numbers = [1, 2, 3, 4, 5]
numbers.pop(2)

# ===========
# LS Solution
# ===========

numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers)  # [1, 2, 4, 5]


# 💡 Summary:
# ┌──────────────┬──────────────────────┬──────────────┬──────────────┬───────────────────────┐
# │ Method       │ Returns removed item?│ Mutates list │ Simple syntax│ Preferred when        │
# ├──────────────┼──────────────────────┼──────────────┼──────────────┼───────────────────────┤
# │ pop(index)   │ ✅ Yes               │ ✅ Yes       │ ✅           │ You need the value    │
# │ del list[i]  │ ❌ No                │ ✅ Yes       │ ✅✅          │ You just want it gone │
# └──────────────┴──────────────────────┴──────────────┴──────────────┴───────────────────────┘
