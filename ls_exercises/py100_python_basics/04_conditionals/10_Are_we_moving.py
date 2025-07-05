# 10. Are we moving?

"""

Determine what the following code snippet prints. First solve it in your head or on paper, 
then run it in your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0

"""

# My response:

# braking force < acceleration is True as 19 < 24.
# (speed > 0 or acceleration > 0) is True as 24 > 0.
# Therefore, True and True is True.

# The parentheses are not required for the specific values assigned to the variables as it would still have resulted in True.
# It would have resulted in: True and False or True which is False or True which is True.
# However, the parentheses are required to output the correct value if the variable values changed. 

# With parentheses: False and (False or True) = False and True = False
# Without parentheses: False and False or True) = False or True = True