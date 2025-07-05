"""
Determine whether the name Dino appears in the strings below -- check each
string separately:

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."
"""

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

if str1.find('Dino') != -1:
    print("str1 contains 'Dino'")
elif str1.find('Dino') == -1:
    print("str1 does not contain 'Dino'")

if str2.find('Dino') != -1:
    print("str2 contains 'Dino'")
elif str2.find('Dino') == -1:
    print("str1 does not contain 'Dino'")
