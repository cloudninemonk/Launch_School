"""
Madlibs is a simple game where you create a story template with "blanks" for
words. You, or another player, then construct a list of words and place them
into the story, creating an often silly or funny story as a result.

Create a simple madlib program that prompts for a noun, a verb, an adverb, and
an adjective, and injects them into a story that you create.

Example:
Enter a noun: dog
Enter a verb: walk
Enter an adjective: blue
Enter an adverb: quickly

Expected Output:
Do you walk your blue dog quickly? That's hilarious!
The blue dog walks quickly over the lazy dog.
The dog quickly walks up to Joe's blue turtle.
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- 4 x user inputs

Output:
-

Rules (Explicit):
- Interpolated string that includes the 4 x user inputs.
- 4 user inputs to be stored in a list

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
- Input:
    Enter a noun: dog
    Enter a verb: walk
    Enter an adjective: blue
    Enter an adverb: quickly
- Output:
    Do you walk your blue dog quickly? That's hilarious!
    The blue dog walks quickly over the lazy dog.
    The dog quickly walks up to Joe's blue turtle.

Edge Cases:
-

D: Data Structures
-------------------------
- strings
- list

Notes
-------------------------
- list indexing

A: Algorithm (Step-by-step)
-------------------------
1. Assign an empty list to a variable
2. Ask the user for four separate inputs, appending each input to the dictionary
3. Print the interpolated string calling on the appropriate element through indexation

C: Code With Intent
-------------------------
"""

details = [
    input('Enter a noun: '),
    input('Enter a verb: '),
    input('Enter an adjective: '),
    input('Enter an adverb: ')
]

print(f"Do you {details[1]} your {details[2]} {details[0]} {details[3]} ? That's hilarious!\n"
f"The {details[2]} {details[0]} {details[1]} {details[3]} over the lazy dog.\n"
f"The {details[0]} {details[3]} {details[1]} up to Joe's {details[2]} turtle.")
