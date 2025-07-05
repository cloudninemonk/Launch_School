"""
Write a function that takes a non-empty string argument and returns the middle
character(s) of the string. If the string has an odd length, you should return
exactly one character. If the string has an even length, you should return exactly
two characters.

Examples:
    print(center_of('I Love Python!!!') == "Py")    # True
    print(center_of('Launch School') == " ")        # True
    print(center_of('Launchschool') == "hs")        # True
    print(center_of('Launch') == "un")              # True
    print(center_of('Launch School is #1') == "h")  # True
    print(center_of('x') == "x")                    # True
"""

def center_of(string):
    str_len = len(string)
    str_centre_index = str_len // 2
    if str_len % 2 != 0:
        return string[str_centre_index]
    return string[str_centre_index-1:str_centre_index + 1]

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True