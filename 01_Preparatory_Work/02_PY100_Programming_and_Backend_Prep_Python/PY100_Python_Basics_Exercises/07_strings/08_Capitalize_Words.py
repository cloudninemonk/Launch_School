# 8. Capitalize Words

"""
Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.
"""

# My response:

text = 'launch school tech & talk'
my_list = text.split()
my_capitalization = []

for word in my_list:
    capital_word = word.capitalize()
    my_capitalization.append(capital_word)

print(' '.join(my_capitalization))

# A more concise way:

text = 'launch school tech & talk'
result = ' '.join(word.capitalize() for word in text.split())





