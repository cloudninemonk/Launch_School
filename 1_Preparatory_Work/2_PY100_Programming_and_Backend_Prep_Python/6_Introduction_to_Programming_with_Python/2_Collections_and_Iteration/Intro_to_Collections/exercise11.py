# Consider the data in the following table:

# Name	        Country

# Alice	        USA
# Francois	    Canada
# Inti	        Peru
# Monika	    Germany
# Sanyu	        Uganda
# Yoshitaka	    Japan

# You need to write some Python code to determine the country name associated with one of the listed names. 
# Your code should include the data structure(s) you need and at least one test case to ensure the code works.


# My response:
origin = {
    'Alice': 'USA', 
    'Francois': 'Canada', 
    'Init': 'Peru', 
    'Monika': 'Germany', 
    'Sanyu': 'Uganda', 
    'Yoshitaka': 'Japan'
}

name = input('What is your name? ')
print(f'Your country of origin is {origin[name]}')


# Launch School's answer:

countries = {
    'Alice':     'USA',
    'Francois':  'Canada',
    'Inti':      'Peru',
    'Monika':    'Germany',
    'Sanyu':     'Uganda',
    'Yoshitaka': 'Japan',       # Note the trailing comma after 'Japan'. It is a stylistic choice that Launch School encourages.
}

print(countries['Monika'])