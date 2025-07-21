"""
Write a function that takes two strings as arguments, determines the length of
the two strings, and then returns the result of concatenating the shorter
string, the longer string, and the shorter string once again. You may assume
that the strings are of different lengths.

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
"""
# ==========
# My Solution
# ==========

def short_long_short(text1, text2):
    if len(text1) < len(text2):
        return text1 + text2 + text1
    else:
        return text2 + text1 + text2

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

# ==========
# LS Solution
# ==========

def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1