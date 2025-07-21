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

def story(noun, verb, adjective, adverb):
    return (
        f"Do you {verb} your {adjective} {noun}? That's hilarious!\n"
        f"The {adjective} {noun} {verb}s {adverb} over the lazy {noun}.\n"
        f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle."
    )

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(story(noun, verb, adjective, adverb))
