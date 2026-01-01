'''
Given a sequence of integers, filter out instances where the same value occurs successively, retaining only the initial occurrence. Return the refined sequence.

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True
'''
# ==========
# My Solution
# ==========
#traditional loop
def unique_sequence(numbers):
    if not numbers:
        return []

    unique = [numbers[0]]
    for value in numbers [1:]:
        if value != unique[-1]:
            unique.append(value)

    return unique

#comprehension
def unique_sequence(numbers):
    return [value for idx, value in enumerate(numbers) if idx == 0 or value != numbers[idx-1]]


original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True

# ==========
# LS Solution
# ==========

# solution 1
def unique_sequence(numbers):
    if not numbers:
        return []

    unique = [numbers[0]]
    for value in numbers[1:]:
        if value != unique[-1]:
            unique.append(value)

    return unique

#solution 2
def unique_sequence(numbers):
    return [value
            for idx, value in enumerate(numbers)
            if idx == 0 or value != numbers[idx-1]]