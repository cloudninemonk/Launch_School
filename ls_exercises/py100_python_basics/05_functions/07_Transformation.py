# 7. Transformation

"""

Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

"""

# My response:

my_str = 'Captain Ruby'
new_str = my_str.replace(my_str.split(' ')[1], 'Python')
print(new_str) # Captain Python

# Comments
"""

# Rather than implementing the my_str.split(' ')[1], I could have implemented 'Ruby' instead.

"""

# Launch School's solution:

"""
Solution 1:

first_8 = 'Captain Ruby'[:8]
new_str = first_8 + 'Python'
print(new_str)      # Captain Python

Solution 2:

all_words = 'Captain Ruby'.split(' ')
first_word = all_words[0]
new_str = first_word + ' Python'
print(new_str)      # Captain Python

Solution 3: 

new_str = 'Captain Ruby'.replace('Ruby', 'Python')
print(new_str)      # Captain Python

"""

