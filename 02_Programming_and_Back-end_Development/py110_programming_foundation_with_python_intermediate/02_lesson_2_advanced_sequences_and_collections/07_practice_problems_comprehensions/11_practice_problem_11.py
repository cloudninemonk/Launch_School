'''
The following dictionary has list values that contains strings. Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, then print it.

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

Start by trying to write this using nested loops.

Extra Challenge: Once your nested loop code works, try to refactor the code so it uses a single list comprehension. (You can print the resulting list outside of the comprehension.)
'''
# ==========
# My Solution
# ==========
# without comprehension - accessing values
VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []

for key in dict1:
    for word in dict1[key]: # dict[key] provides the list to iterate through
        for char in word:
            if char in VOWELS:
                list_of_vowels.append(char)

print(list_of_vowels)

# alternative - accessing values through a dict.values() view object

VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = []

for value in dict1.values():
    for word in value:
        for char in word:
            if char in VOWELS:
                list_of_vowels.append(char)

print(list_of_vowels)
# with comprehension
VOWELS = 'aeiou'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = [char for key in dict1 for word in dict1[key] for char in word if char in VOWELS]
print(list_of_vowels)