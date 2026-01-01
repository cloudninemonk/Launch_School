'''
Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
'''
# ==========
# LS Solution
# ==========
# traditional loop
def remove_vowels(strings):
    new_strings = []
    for string in strings:
        s = ''
        for char in string:
            if char not in 'aeiou':
                s += char
        new_strings.append(s)
    return new_strings

# list comprehension
VOWELS = 'aeiouAEIOU'

def strip_vowels(string):
    return ''.join([char for char in string if char not in VOWELS])

def remove_vowels(strings):
    return [strip_vowels(string) for string in strings]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# ==========
# LS Solution
# ==========
def strip_vowels(string):
    VOWELS = "aeiouAEIOU"
    no_vowels = [char for char in string
                 if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(string_list):
    return [strip_vowels(string) for string in string_list]