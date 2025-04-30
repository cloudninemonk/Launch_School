# 4. What Color?

"""
Using the following code, select and print the value 'blue' from the car object:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
"""

# My response:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

lst = []
for value in car.values():
    lst.append(value)
print(lst[1])\

# LSBot's comments:

print(car['color'])

"""
I was impressed by your ability to work with dictionary methods and iterate 
through values! For dictionary operations specifically, I recommend focusing 
on using keys to directly access values when you know which value you need. 
This approach is more readable, efficient, and maintains the semantic 
relationship between keys and values that dictionaries are designed for.

While your solution works for the current dictionary structure, direct key 
access (car['color']) is both simpler and more resilient to potential changes 
in the dictionary. As you continue in your Python journey, remember that 
sometimes the simplest solution is the most robust one!
"""