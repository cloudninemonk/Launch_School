'''
We have a list of lists and want to duplicate it. After making the copy, we modify the original list, but the copied list also seems to be affected:

What's wrong here? How can you fix it?

import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])
'''
# A shallow copy has been performed on the original list. i.e., only the outer shell is duplicated whilst all the elements within the copied list are direct references to the objects within the original list. To avoid this behaviour, a deep copy is required by using the deepcopy method rather than copy method.
# ==========
# My Solution
# ==========
import copy

original = [[1], 2, [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# ==========
# LS Solution
# ==========
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])  # True
