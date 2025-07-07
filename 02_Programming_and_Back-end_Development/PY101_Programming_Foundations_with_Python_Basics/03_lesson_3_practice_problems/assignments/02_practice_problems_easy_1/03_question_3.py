"""
Starting with the string:

famous_words = "seven years ago..."

Show two different ways to create a new string with "Four score and " prepended
to the front of the string referenced by famous_words.
"""
# 1.
famous_words = "seven years ago..."
famous_words = f"Four score and {famous_words}"
print(famous_words)

#2.
famous_words = "seven years ago..."
famous_words = "Four score and " + famous_words
print(famous_words)

"""
LS Solution
"""

# 1.
# String concatenation
new_string = "Four score and " + famous_words

# 2.
# String interpolation
new_string = f"Four score and {famous_words}"