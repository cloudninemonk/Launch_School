"""
Write a function that returns the next to last word in the string argument.

Words are any sequence of non-blank characters.

You may assume that the input string will always contain at least two words.

Examples:
    # These examples should print True
    print(penultimate("last word") == "last")
    print(penultimate("Launch School is great!") == "is")
"""

def second_last_word(string):
    list_ = string.split()
    return list_[-2]

string = input("Enter a string: ")
print(f"The second last word of the string you entered is '{second_last_word(string)}'.")

