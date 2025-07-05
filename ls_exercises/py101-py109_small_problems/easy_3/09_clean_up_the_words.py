"""
Given a string that consists of some words and an assortment of non-alphabetic
characters, write a function that returns that string with all of the
non-alphabetic characters replaced by spaces. If one or more non-alphabetic
characters occur in a row, you should only have one space in the result (i.e.,
the result string should never have consecutive spaces).

Example:
print(clean_up("---what's my +*& line?") == " what s my line ")
# True
"""

# def clean_up(string):
#     clean_string = ''
#     iterator = 0
#     while iterator < len(string) - 1:
#         if not string[iterator].isalpha():
#             if string[iterator + 1].isalpha():
#                 clean_string += ' '
#                 iterator += 1
#             else:
#                 not string[iterator + 1].isalpha()
#                 iterator += 1
#         elif string[iterator].isalpha():
#             clean_string += string[iterator]
#             iterator += 1

#     print(clean_string)
#     return clean_string

# print(clean_up("---what's my +*& line?") == " what s my line ")

# def clean_up(string):
#     clean_string = ''
#     for char in string:
#         if char.isalpha():
#             clean_string += char
#         else:
#             clean_string += ' '
#     clean_list = clean_string.split('  ')

#     return ''.join(clean_list)

# print(clean_up("---what's my +*& line?") == " what s my line ")

def clean_up(string):
    clean_string = ''
    prev_is_clean = False

    for char in string:
        if char.isalpha():
            clean_string += char
            prev_is_clean = False
        elif not prev_is_clean:
            clean_string += ' '
            prev_is_clean = True

    return clean_string

print(clean_up("---what's my +*& line?") == " what s my line ")