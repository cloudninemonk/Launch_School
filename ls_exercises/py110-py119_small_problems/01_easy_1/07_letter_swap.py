'''
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string of words separated by spaces

Output:
- boolean

Rules (Explicit):
- every word contains at least one character
- input string will always contain at least one word
- no leading or trailing spaces

Rules (Implicit/Inferred):
- words can be made up of any characters

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- function to return a string
- split method
- for loop to iterate through words
- string slicing

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string to the function swap.
2. Split the string with the delimiter as spaces. i.e., no argument in the split method, and assign to words.
3. Assign an empty list to new_words
4. Iterate through words one word at a time.
5. Concatenate the last character followed by the next to first through to next to last, inclusive, followed by the first character, to word.
6. Add word to the list new_words
7. After iterating through each word, return the joined new_words with a space between each.


C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def swap(text):
    words = text.split()
    new_words = []

    for word in words:
        if len(word) > 1:
            word = word[-1] + word[1:-1] + word[0]
        new_words.append(word)

    return ' '.join(new_words)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# ==========
# LS Solution
# ==========

def swap(words):
    words_list = words.split()

    for idx in range(len(words_list)):
        words_list[idx] = swap_first_last_characters(words_list[idx])

    return ' '.join(words_list)

def swap_first_last_characters(word):
    if len(word) == 1:
        return word

    return word[-1] + word[1:-1] + word[0]
