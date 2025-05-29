# 6. Vocabulary

"""
You've been given a list of vocabulary words grouped into sub-lists, by meaning. 
This is a two-dimensional list or a nested list. Write some code that iterates 
through and prints all the words, one per line.

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...
"""

# My response:

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for lsts in vocabulary: # iterates through the vocabulary list
    for feeling in lsts: # Iterates through each vocabulary nested list
        print(feeling)  # Prints the string in each nested list

# LSBot's comments:

"""
One small suggestion would be to consider using even more descriptive variable names. 
For example, instead of lsts, you could use synonym_group or word_group to more 
precisely indicate what each sublist represents in this context.

Your solution is already well-implemented, so this is just a minor stylistic suggestion. 
You've demonstrated a solid understanding of working with nested lists, which will be 
an important skill as you continue in your programming journey.
"""