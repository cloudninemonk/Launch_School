'''
Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.

Words consist of any sequence of non-space characters.

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string of words

Output:
- boolean

Rules (Explicit):
- words can be separated by none or multiple spaces
- dictionary keys and values to be integers

Rules (Implicit/Inferred):
- if string is empty, return empty dictionary
- punctuation is to be included as a character
- spaces to not be included

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- for loop
- split method
- function to return a dictionary

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string to the function word_sizes
2. Assign an empty dictionary to word_sizes_dict
3. Split the string with spaces as the delimiter i.e., no argument required for the split method, and assign to the list words_list.
4. Loop through the words_list and determine the length of each word. Determine if the length of the current word already exists as a key in words_sizes_dict and apply a default value of 0. Update the value by 1.
5. Return the dictionary once the looping has been completed.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def word_sizes(string):
    words_sizes_dict = {}
    words_list = string.split()
    for word in words_list:
        words_sizes_dict[len(word)] = words_sizes_dict.get(len(word), 0) + 1

    return words_sizes_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})

# ==========
# LS Solution
# ==========
def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        word_size = len(word)
        if word_size not in counts:
            counts[word_size] = 0

        counts[word_size] += 1

    return counts

