"""
Write a function that takes a string argument and returns a new string that
contains the value of the original string with all consecutive duplicate
characters collapsed into a single character.

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
"""
# ==========
# My Solution
# ==========
# def crunch(string):
#     if not string:
#         return string
#     new_string = string[0]
#     index = 1
#     while index < len(string):
#         if string[index] != string[index-1]:
#             new_string += string[index]
#         index += 1

#     return new_string


def crunch(string):
    new_string = ''
    for i in range(len(string)):
        if i != len(string) - 1 and string[i] != string [i + 1] or i == len(string) - 1:
            new_string += string[i]
    return new_string


print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# ==========
# LS Solution
# ==========
def crunch(text):
    index = 0
    crunched_text = ''

    while index < len(text):
        if index == len(text) - 1 or text[index] != text[index + 1]:
            crunched_text += text[index]

        index += 1

    return crunched_text
