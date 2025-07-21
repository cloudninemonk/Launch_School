"""
Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

Example:
    repeat('Hello', 3)

Output:
    Hello
    Hello
    Hello
"""

# def repeat(string, number):
#     iteration = 0
#     while iteration < number:
#         print(string)
#         iteration += 1

def repeat(string, number):
    for _ in range(number):
        print(string)

repeat('hello', 3)