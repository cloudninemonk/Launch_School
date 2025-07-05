# 3. Add + Delete

"""
We are given the following list of energy sources.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.
"""

# My response:

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.pop(0)   # removes element, 'fossil', at index 0 from the list
energy.append('geothermal') # appends 'geothermal' to the list

# LSBot comments:
"""
Your solution is well-executed! One consideration worth mentioning is that while pop(0) works 
perfectly in this specific case where we know 'fossil' is at index 0, the remove() method (as 
shown in the solution) might be more appropriate if you didn't know the exact position of the 
element you wanted to remove. The remove() method searches for a specific value rather than 
relying on an index. This makes your code more maintainable if the list order changes in the 
future. That said, both approaches are valid, and your solution demonstrates a good 
understanding of list manipulation in Python.

I'm impressed by your clean code implementation and thoughtful comments. You seem ready to 
tackle more complex problems in the course!

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')
print(energy)
# ['solar', 'wind', 'tidal', 'fusion', 'geothermal']
"""