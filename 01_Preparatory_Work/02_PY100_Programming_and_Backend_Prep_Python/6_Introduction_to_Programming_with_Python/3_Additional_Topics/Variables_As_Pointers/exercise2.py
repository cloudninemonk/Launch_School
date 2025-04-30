# Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)


# My response:

# {42, 'Monty Python', ('a', 'b', 'c')}


# Launch School's answer:

# The order of the elements probably won't match,
# but the 4 elements shown here should all be
# present in your answer.

# {('a', 'b', 'c'), 'Monty Python', 42, range(5, 10)}

# This result demonstrates that set1 and set2 reference the same set: if we add an element to set1, 
# we'll see that element when we look at set2. The opposite is true, too: if we add something to set2, 
# we'll see it in set1.

# This code also demonstrates that assigning a variable to another variable doesn't create a new object. 
# Instead, Python copies a reference from the original variable (set1) into the target variable (set2).