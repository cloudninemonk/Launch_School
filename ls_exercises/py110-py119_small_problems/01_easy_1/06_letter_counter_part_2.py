'''
Modify the word_sizes function from the previous exercise to exclude non-letters when determining word size. For instance, the word size of "it's" is 3, not 4.

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

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
- non-letter characters to be excluded from the word size determination.

Rules (Implicit/Inferred):
- numbers to not be included in word size

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

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
- isalpha method
- function to return a dictionary

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string to the function word_sizes
2. Assign an empty dictionary to word_sizes_dict
3. Split the string with spaces as the delimiter i.e., no argument required for the split method, and assign to the list words_list.
4. Loop through the words_list and assign an empty string to current_word.
5. Loop through each character of the current word. Determining if the character is alpha the length of each word. Determine if the length of the current word already exists as a key in words_sizes_dict and apply a default value of 0. Update the value by 1.
5. Return the dictionary once the looping has been completed.

C: Code With Intent
-------
"""
# ==========
# My Solution
# ==========
def word_sizes(string):
    words_sizes_dict = {}
    words_list = string.split()

    for word in words_list:
        current_word = ''
        for char in word:
            if char.isalpha():
                current_word += char
        current_word_size = len(current_word)
        if current_word_size == 0:
            continue
        words_sizes_dict[current_word_size] = words_sizes_dict.get(current_word_size, 0) + 1

    return words_sizes_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})
co
string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})

print(word_sizes("123 !!!") == {})

print(word_sizes("hi! 123 @#$ good-day") == {2: 1, 7: 1})
# ==========
# LS Solution
# ==========
def remove_non_letters(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char

    return result

def word_sizes(words):
    words_list = words.split()
    counts = {}

    for word in words_list:
        clean_word = remove_non_letters(word)

        clean_word_size = len(clean_word)
        if clean_word_size == 0:
            continue

        if clean_word_size not in counts:
            counts[clean_word_size] = 0

        counts[clean_word_size] += 1

    return counts