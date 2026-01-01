'''
Write another function that returns True if the string passed as an argument is a palindrome, or False otherwise. This time, however, your function should be case-insensitive, and should ignore all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome function you wrote in the previous exercise.

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

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
- boolean

Rules (Explicit):
- case-insensitive
- ignore all non-alphanumeric characters

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True


Edge Cases:
-

D: Data Structures
-------------------------
-

Notes
-------------------------
- loop(for)
- isalnum method for checking if character is alphanumeric

A: Algorithm (Step-by-step)
-------------------------
1. Pass the string, original_string to the function is_palindrome
2. Loop through each character of original_string and check if character is alphanumeric.
3. Concatenate a new string, new_string, with all alphanumeric characters.
3. Return the boolean that results from checking if the new_string is equal to the reverse of new_string

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
def is_real_palindrome(original_string):
    new_string = ''
    for character in original_string:
        if character.isalnum():
            new_string += character.lower()
        # print(new_string)
        # print(new_string[::-1])

    '''Return True if new_string reads the same as the reverse of new_string'''
    return new_string == new_string[::-1]

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True

# ==========
# LS Solution
# ==========
# First, we'll reuse the is_palindrome function:
def is_palindrome(s):
    return s == s[::-1]

# Now, let's implement is_real_palindrome:
def is_real_palindrome(s):
    cleaned_string = ''
    for char in s:
        if char.isalnum():
            cleaned_string += char.casefold()

    return is_palindrome(cleaned_string)