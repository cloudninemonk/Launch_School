# 7. Dictionary Access

"""
You are trying to access a value in a dictionary, but the code is 
giving you an error. Can you change line 3 so that it prints 
"Unknown" instead of raising an error?

info = {'name': 'Srdjan', 'age': 38}

print(info['city'])

"""

# My response:

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))

# Alternative solution:

print('Unknown' if 'city' not in info else True)
