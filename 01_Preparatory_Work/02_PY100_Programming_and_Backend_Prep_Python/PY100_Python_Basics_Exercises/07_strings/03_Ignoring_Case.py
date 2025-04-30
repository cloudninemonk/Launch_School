# 3. Ignoring Case

"""
Using the following code, compare the value of name with the string 'RoGeR' 
while ignoring the case of both strings. Print true if the values are the 
same; print false if they aren't. Next, perform a case-insensitive comparison 
between the value of name and the string 'DAVE'.

name = 'Roger'
"""

# My response:

name = 'Roger'
text = 'RoGeR' 
text1 = 'Dave'

print(True if name == text else False) # False
print(True if name.casefold() == text.casefold() else False) # True
print(True if name.casefold() == text1.casefold() else False) # False

# Comments:

"""
The expressions like True if name == text else False are redundant. 
Since name == text already returns a boolean (True or False), the ternary 
operator isn’t needed. It can simply be print(name == text).
This applies to all three print statements. While not a PEP 8 violation, 
it’s un-Pythonic and less readable.

Your understanding of the issue with the redundant expressions is excellent, 
but you haven't applied this knowledge to your updated solution. I encourage 
you to simplify your print statements as you suggested earlier, and ensure 
you're using 'DAVE' (uppercase) for the second comparison as specified in the 
exercise.

Here's how your solution could be improved:

name = 'Roger'

print(name.casefold() == 'RoGeR'.casefold())  # True
print(name.casefold() == 'DAVE'.casefold())   # False

"""




