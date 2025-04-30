# Write a comprehension that creates a dict object whose keys are strings and whose values are the length of the corresponding key. 
# Only keys with odd lengths should be in the dict. Use the set given by my_set as the source of strings.

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# My response:

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_keys = [ word for word in my_set             # Create a list of the names that are odd in length
           if len(word) % 2 != 0 ]              
my_values = [ len(word) for word in my_keys ]   # Create a list of the length of each name in my_keys
my_dict = dict(zip(my_keys, my_values))         # Zip the two lists and convert to a dictionary
# {'Cocoa': 5, 'Cheddar': 7, 'Pudding': 7}

# Comments:
# Despite arriving at the correct output, the method adopted is not concise. The wording of LS's question is not precise, 
# however, it should be interpreted that the expected code would be a single comprehension as demonstrated in LS's answer.


# Launch School's answer:

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0 }
print(result)
# {'Cheddar': 7, 'Pudding': 7, 'Cocoa': 5}

# Remember: sets are unordered, so your result may have a different ordering.