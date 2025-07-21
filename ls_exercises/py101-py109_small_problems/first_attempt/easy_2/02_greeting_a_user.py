"""
Write a program that asks for user's name, then greets the user. If the user appends
a ! to their name, the computer will yell the greeting (print it using all uppercase).

Example 1:
    What is your name? Sue
    Hello Sue.

Example 2:
    What is your name? Bob!
    HELLO BOB! WHY ARE WE YELLING?
"""

# def greetings(name):
#     "Return a greeting in uppercase if input included '!'"
#     for char in name:
#         if char == '!':
#             return f"HELLO {name.upper()}! WHY ARE WE YELLING?"
#     return f"Hello {name.capitalize()}."

def greetings(name):
    if '!' in name:
        return f"HELLO {name.upper()} WHY ARE WE YELLING?"
    return f"Hello {name.capitalize()}."

name = input("What is your name? ")
greeting = greetings(name)
print(greeting)
