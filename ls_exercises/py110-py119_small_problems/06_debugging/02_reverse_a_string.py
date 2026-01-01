'''
You have a function that is supposed to reverse a string passed as an argument. However, it's not producing the expected output. Explain the bug, and provide a solution.

def reverse_string(string):
    for char in string:
        string = char + string
    print(string)

    return string

print(reverse_string("hello") == "olleh")
'''

# ==========
# My Solution
# ==========
# In the function, the passed string argument is assigned to the parameter string. The string variable is then reassigned on each iteration of the for loop to the current character + the previous string. First iteration string = 'h' + 'hello' = 'hhello'. Second iteration: string = 'e' + 'hhello' = 'ehhello'

#A soution would be to implement a reverse slice.

def reverse_string(string):
    return string[::-1]

print(reverse_string("hello") == "olleh")

# ==========
# LS Solution
# ==========
# solution 1
def reverse_string(string):
    reversed_str = ""
    for char in string:
        reversed_str = char + reversed_str

    return reversed_str

print(reverse_string("hello") == "olleh")  # True

# solution 2
def reverse_string(string):
    return string[::-1]

print(reverse_string("hello") == "olleh")  # True

