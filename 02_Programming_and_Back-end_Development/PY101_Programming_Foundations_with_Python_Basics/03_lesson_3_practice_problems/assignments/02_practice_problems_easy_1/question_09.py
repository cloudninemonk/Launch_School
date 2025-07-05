"""
Print a new version of the sentence given by advice that ends just before the
word house. Don't worry about spaces or punctuation: remove everything starting
from the beginning of house to the end of the sentence.

advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
"""

advice = "Few things in life are as important as house training your pet dinosaur."
advice = advice.removesuffix('house training your pet dinosaur.')
print(advice)

"""
Chat GPT Solution
"""
advice = "Few things in life are as important as house training your pet dinosaur."
index = advice.find('house')
advice = advice[:index]
print(advice)


"""
LS Solution
"""
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.split('house')[0])