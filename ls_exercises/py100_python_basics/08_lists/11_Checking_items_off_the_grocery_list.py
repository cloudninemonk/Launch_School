# 11. Checking items off the grocery list

"""
We have a grocery list. As we check off items on that list, from the top of the list to the bottom, we want to remove them from the list.

Write code that removes the items from grocery_list, one by one, until it is empty. 
If you print the elements you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

print(grocery_list)

Expected output:

paprika
tofu
garlic
quinoa
carrots
broccoli
hummus
[]

"""

# My response:

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']
while grocery_list != []:
    print(grocery_list.pop(0))

print(grocery_list)

# LSBot comments:

"""
Your solution is very well-written for this simple task! A small suggestion would 
be to use the implicit truthiness of non-empty lists in Python. Instead of checking 
grocery_list != [], you could simplify to just while grocery_list:, which reads as 
"while grocery_list is not empty" and is a more Pythonic way to express the same 
condition. This is a minor optimization that helps make your code even more concise 
and idiomatic.

Overall, your solution is elegant and demonstrates a good grasp of Python list operations. 
You're ready to tackle more complex problems!
"""