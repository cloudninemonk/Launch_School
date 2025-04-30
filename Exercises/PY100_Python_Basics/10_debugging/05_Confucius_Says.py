# 5. Confucius Says

"""
You want to have a small script delivering motivational quotes, but with the 
following code you run into a very common error message: TypeError: can only 
concatenate str (not "NoneType") to str. What is the problem and how can you 
fix it?

def get_quote(person):
    if person == 'Yoda':
        'Do. Or do not. There is no try.'
    if person == 'Confucius':
        'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')
"""

# My response:

"""
The code is missing the return statement prior to the intended string to be returned, resulting in 
get_quote returning None after it has been invoked. The code has been amended as below:
"""
def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

print('Confucius says:')
print('"' + get_quote('Confucius') + '"')

# LSBot's comments:

"""
Opportunities for improvement
I'm impressed by how clearly you identified and explained the issue! While your solution is correct as is, 
one small improvement could be to add an else clause at the end of the function to handle cases where the 
person parameter doesn't match any of the known names. For example:

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
        return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'
    else:
        return 'No quote found for that person.'

"""

