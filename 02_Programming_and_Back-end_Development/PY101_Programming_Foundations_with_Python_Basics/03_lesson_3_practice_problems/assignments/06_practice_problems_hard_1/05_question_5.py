"""
What do you expect to happen when the greeting variable is referenced in the
last line of the code below?

if False:
    greeting = "hello world"

print(greeting)
"""

# ==========
# My Solution
# ==========

# I recognised there would be an error without actually knowing why. More so an
# educated guess.

# ==========
# LS Solution
# ==========

# In Python, referencing an uninitialized variable will result in a NameError
# being raised. This is because the if block is not executed due to the False
# condition, and hence, the greeting variable is never initialized.

# ==========
# Comments from ChatGPT
# ==========

# What does if False: do in Python?

# if False:
#     # block of code

# It’s a conditional statement that tells Python:
#   "Only run the block of code if the expression False evaluates to True."
# Since False is always false (a constant boolean literal), the block never executes.
