# 3. Broken Odometer

"""
Using the following code, delete the 'mileage' key and its associated value from car.

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}
"""

# My response:

car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year':    2003,
}

car.pop('mileage')

# LSBot's comments:

"""
I was impressed by your knowledge of using an alternative method to solve the problem! 
Both pop() and del are commonly used for removing items from dictionaries. One small 
difference worth noting is that while pop() returns the removed value, del does not. 
For situations where you don't need the removed value, del might be considered slightly 
more direct. However, your solution using pop() is excellent and demonstrates flexibility 
in approaching Python problems.

If you wanted to explore even more options, you could also look into the dict.popitem() 
method which removes and returns the last inserted key-value pair (useful in other contexts), 
though it wouldn't be appropriate for this specific task where a particular key needs to 
be removed.
"""