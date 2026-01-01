'''
Write a function that takes a list of integers between 0 and 19 and returns a list of those integers sorted based on the English word for each number:

zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- list of integers

Output:
- function: list of integers
- program: boolean

Rules (Explicit):
-

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- sort/sorted function
- key function

A: Algorithm (Step-by-step)
-------------------------
1a. Initialise a list input_list of all the integers 0 to 19.
1b. Initialise expected_result to the returned value from alphabetic_number_sort
2. Pass the input_list of integers to function alphabetic_number_sort
3. Initialise sorted_list to the sorting of input_list based on the key function number_to_word
4a. Define the number_to_word to receive num from the iteration through the input_list occurring when intialising sorted_list
4b. Initialise words_of_numbers to contain the worded numbers zero to nineteen.
4c. Return the worded number from words_of_numbers at the given num.
5. Return sorted_list from alphabetic_number_sort


C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
WORDS_OF_NUMBERS = ['zero', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',   'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

def number_to_word(num):
    return WORDS_OF_NUMBERS[num]

def alphabetic_number_sort(input_list):
    sorted_list = sorted(input_list, key = number_to_word)
    return sorted_list

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = alphabetic_number_sort(input_list)
print(alphabetic_number_sort(input_list) == expected_result)

# ==========
# LS Solution
# ==========

NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five',
                'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                'twelve', 'thirteen', 'fourteen', 'fifteen',
                'sixteen', 'seventeen', 'eighteen', 'nineteen']

def word_for_number(num):
    return NUMBER_WORDS[num]

def alphabetic_number_sort(numbers):
    return sorted(numbers, key=word_for_number)

