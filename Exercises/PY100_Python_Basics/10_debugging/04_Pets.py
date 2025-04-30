# 4. Pets

"""
Magdalena has just adopted a new pet! She wants to add her new dog, 
Bowser, to the pets dictionary. After doing so, she realizes that 
her dogs Sparky and Fido have been mistakenly removed. Help Magdalena 
fix her code so that all three of her dogs' names will be associated 
with the key 'dog' in the pets dictionary.

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'] = 'bowser'

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}
"""

# My response:

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')

print(pets)  # Output: {'cat': 'pepe', 'dog': ['sparky', 'fido', 'bowser'], 'fish': 'oscar'}

# LSBot's comments:

"""
Opportunities for improvement
I was impressed by your clean solution! Your code works perfectly and is easy to understand. 
Since this was a straightforward debugging exercise, there's not much to improve upon. As 
you progress in your Python learning journey, you'll encounter more complex data structures 
and operations. This solution shows you've grasped the fundamentals of working with nested 
data structures (a list inside a dictionary), which is an important skill that will serve 
you well in more complex problems.
"""