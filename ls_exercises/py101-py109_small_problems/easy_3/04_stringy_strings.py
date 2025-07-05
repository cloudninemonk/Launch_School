"""
Write a function that takes one argument, a positive integer, and returns a
string of alternating '1's and '0's, always starting with a '1'. The length of
the string should match the given integer.

Examples:
    print(stringy(6) == "101010")           # True
    print(stringy(9) == "101010101")        # True
    print(stringy(4) == "1010")             # True
    print(stringy(7) == "1010101")          # True
"""
def stringy(number):
    binary_string = ''

    for _ in range(number):
        if _ % 2 == 0:
            binary_string += '1'
        else:
            binary_string += '0'
    print(binary_string)
    return binary_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True

