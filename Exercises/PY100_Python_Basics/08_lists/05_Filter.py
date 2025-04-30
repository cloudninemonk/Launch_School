# 5. Filter

"""
Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]
"""

# My response:

# 1. 
scores = [96, 47, 113, 89, 100, 102]
print(len([score for score in scores if score >= 100]))

# 2.
scores = [96, 47, 113, 89, 100, 102]
counter = 0

for score in scores:
    if score >= 100:
        counter += 1
print(counter)

# LSBot's comments:
"""
If you're interested in exploring further, you might also look into the filter() function 
or the sum() function with a condition as another way to solve this type of problem:

print(sum(1 for score in scores if score >= 100))
"""