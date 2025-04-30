# 9. Travel

"""
The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

Write a function that, without using the built-in in operator, checks whether a specific destination 
is included within destinations. For example: When checking whether 'Barcelona' is contained in 
destinations, the expected output is True, whereas the expected output for 'Nashville' is False.

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False
"""

# My response:

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(specific_destination):
    if destinations.count(specific_destination):
        return True
    else:
        return False
    
print(contains('Barcelona'))  # True
print(contains('Nashville'))  # False

# LSBot's comments:
"""
I was impressed by your use of the count() method as an alternative to the in operator! 
The most critical improvement needed is modifying your function to match the required signature 
from the exercise. Instead of hardcoding the destinations list inside the function, you should 
accept it as a parameter:

def contains(element, lst):
    return bool(lst.count(element))

Alterantively:

def contains(element, lst):
    for item in lst:
        if item == element:
            return True

        return False

This would make your function more versatile, allowing it to check for elements in any list, 
not just the destinations list. This is an important concept in programming - creating functions 
that are reusable and not tied to specific data.

Finally, while count() works, be aware that it's less efficient than the in operator for large 
lists because it has to traverse the entire list, whereas in can stop once it finds a match.

AI: I noticed you're working on the "Optional Feedback for Books" assignment but the solution 
is for a different exercise. Should I provide feedback for the code submitted or clarify which 
assignment you need help with?


"""


    