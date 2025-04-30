# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of my_list. In this problem, 
# you should write code that creates a new list with one element for each number in my_list. 
# If the original number is an even, then the corresponding element in the new list should 
# contain the string 'even'; otherwise, the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# Expected output:
# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]


# My response:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]
my_evens_and_odds = []
my_str = ''

for number in my_list:
    if number % 2 == 0:
        my_str = 'even'
    else:
        my_str = 'odd'
    my_evens_and_odds.append(my_str)
print (my_evens_and_odds)

# Comments:
# No need to include my_str variable. Can directly append a string to my_evens_and_odds.


# Launch School's answer:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)

# Our approach is straightforward: we iterate over all the numbers in the list and check whether each is even. 
# Based on the result, we append either 'even' or 'odd' to the result list.

# You may have struggled if you tried to use a list comprehension for this problem. 
# Since comprehensions don't have an else capability, trying to generate 'even' for some values and 'odd' for others is challenging. 
# You can use a ternary expression in the comprehension, but this is a little confusing visually:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = [ 'even' if number % 2 == 0 else 'odd'
           for number in my_list ]
print(result)

# On line 75, we've used a ternary expression to choose between the two values. The ternary is equivalent to:

if number % 2 == 0:
    return 'even'
else:
    return 'odd'

# A cleaner approach is to use a helper function to determine whether we should add 'even' or 'odd' to the new list:

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
           for number in my_list ]
print(result)