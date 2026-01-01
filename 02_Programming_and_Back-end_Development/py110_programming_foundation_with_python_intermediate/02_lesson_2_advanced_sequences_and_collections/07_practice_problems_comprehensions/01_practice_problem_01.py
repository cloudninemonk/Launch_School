'''
Consider the following nested dictionary:

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

The result should be 444.
'''
# ==========
# My Solution
# ==========

# for loop
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_age = 0
for details in munsters.values():
    if details['gender'] == 'male':
        total_age += details['age']
print(total_age)

# comprehension

total_age = sum([details['age'] for details in munsters.values() if details['gender'] == 'male'])
print(total_age)

# ==========
# LS Solution
# ==========

# loop
total_male_age = 0
for member in munsters.values():
    if member['gender'] == 'male':
        total_male_age += member['age']

print(total_male_age)         # 444

# comprehension
all_male_ages = [member['age'] for member in munsters.values()
                               if member['gender'] == 'male']

print(sum(all_male_ages))     # 444




