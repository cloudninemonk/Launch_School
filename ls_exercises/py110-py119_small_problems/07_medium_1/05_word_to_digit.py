'''
Write a function that takes a string as an argument and returns that string with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its corresponding digit character.

You may assume that the string does not contain any punctuation.

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string

Output:
- string

Rules (Explicit):
- String argument does not contain any punctuation.

Rules (Implicit/Inferred):
-

Mental Model (Optional):
- Function to receive a string argument. String argument to be checked for whereever there are number words and those words to be converted to integers.

E: Examples / Test Cases
-------------------------
message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

Edge Cases:
-

D: Data Structures
-------------------------
- dictionary

Notes
-------------------------
- list comprehension

A: Algorithm (Step-by-step)
-------------------------
1. Initialise a constant numbers with the number word as the key and number integer as the value for number words zero to nine, inclusive.
2. Function word_to_digit to receive the string argument message.
3. Iterate through the enumerate of the message split into a list, checking if the current word is contained within numbers constant.
4. If it is contained, return the corresponding value and replace the element at the current index with the value.
5. Add each element to a new list words_to_digits_list.
6. Return the joining of the words_to_digits_list.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

NUMBERS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
# traditional loop


def word_to_digit(message):
    words_to_digits = []

    for word in message.split():
        if word in NUMBERS:
            words_to_digits.append(NUMBERS[word])
        else:
            words_to_digits.append(word)
    return ' '.join(words_to_digits)

# list comprehension
def word_to_digit(message):
    words_to_digits = [NUMBERS[word] if word in NUMBERS else word for word in message.split()]
    return ' '.join(words_to_digits)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# ==========
# LS Solution
# ==========
NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

def word_to_digit(sentence):
    words = sentence.split()
    processed_words = [NUM_WORDS.get(word, word) for word in words] # get returns the value if word is in the dictionary, defaults to word if not
    return ' '.join(processed_words)

# further exploration
'''
Can you solve this problem if the individual words can end with punctuation? For instance:

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")
# Should print True

You can get the list of all punctuation characters from the string.punctuation variable in the string module:

import string
print(string.punctuation)
'''
# ==========
# My Solution
# ==========
# assume words can end with only one punctuation character.

import string

PUNCTUATION = string.punctuation

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}


def word_to_digit(sentence):
    def convert(word):
        stripped_word = word.strip(PUNCTUATION)
        digit = NUM_WORDS.get(stripped_word, stripped_word)
        if word[-1] in PUNCTUATION:
            return digit + word[-1]
        return digit

    processed_words = [convert(word) for word in sentence.split()]
    return ' '.join(processed_words)

message = 'Please call me at five, five, five, one, two, three, four.'
print(word_to_digit(message) == "Please call me at 5, 5, 5, 1, 2, 3, 4.")

# ==========
# LS Solution
# ==========
# this solution accounted for cases of leading and trailing punctuation. There could be more than one punctuation character in sequence.

import string

NUM_WORDS = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}

PUNCTUATION = string.punctuation

def word_to_digit(sentence):
    result = []

    for token in sentence.split():
        # Separate leading and trailing punctuation
        start = 0
        end = len(token)

        while start < end and token[start] in PUNCTUATION: # continues looping until False
            start += 1
        while end > start and token[end - 1] in PUNCTUATION: # continues looping until False
            end -= 1

        leading = token[:start]
        core = token[start:end]
        trailing = token[end:]

        replacement = NUM_WORDS.get(core, core)
        result.append(f"{leading}{replacement}{trailing}")

    return ' '.join(result)

