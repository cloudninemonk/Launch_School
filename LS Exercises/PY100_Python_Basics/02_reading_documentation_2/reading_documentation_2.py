# 1. String Formatting
# Python offers multiple ways to format strings. The str.format method is a popular method, but since Python 3.6, 
# a new way called f-strings (formatted string literals) was introduced. F-strings offer a concise way to embed 
# expressions inside string literals.

# Given the following variables:

name = "Victor"
profession = "programmer"

# a. How can you print the string Hello, Victor. You are a programmer. using the str.format method? 
# You should fill in the name and profession in a string literal that contains the rest of the text.

message_format = "Hello, {}. You are a {}."
formatted_message = message_format.format(name, profession)
print(formatted_message)
# Hello, Victor. You are a programmer.


# b. How can you achieve the same result using an f-string?

fstring = f'Hello, {name}. You are a {profession}.'
print(fstring)
# Hello, Victor. You are a programmer.


# 2. Style Guide
# In the following code snippet, find all violations of the PEP8 style guide. Rewrite it so that it conforms with the guide. 

iceCreamDensity=10              

while iceCreamDensity>0 :
    print('Drip...')
    iceCreamDensity-=1

print('The ice cream melted.')

# all characters for the variable should be lowercase i.e. snake_case
# should be a space before and after =
iceCreamDensity=10

# should be a space before and after >
# should not be a space between 0 and :
while iceCreamDensity>0 :

    print('Drip...')
    # should be a space before - and after =
    iceCreamDensity-=1
    
print('The ice cream melted.')


# Rewritten so it conforms with the guide.

icecreamdensity = 10

while icecreamdensity > 0:
    print('Drip...')
    iceCreamDensity -= 1

print('The ice cream melted.')


# 3. Arithmetic Operator Precedence

# Find the Python Documentation on operator precedence, and use it to determine the result of evaluating 4 * 5 + 3**2 / 10.

# Section 6.17 - Operator precendence.
# For 4 * 5 + 3**2 / 10:
# ** has the highest precedence followed by * and , which have the same precedence. 
# + has the lowest precedence.

# Step 1: 3**2 # 9
# Step 2: 4 * 5 is 20 and 9 / 10 which is 0.9.
# Step 3: 20 + 0.9 which is 20.9

my_calc = 4 * 5 + 3**2 / 10 
print(my_calc) # 20.9


# 4. Date

# Using the datetime module in Python, how would you obtain the current date and time?

# classmethod datetime.now(tz=None)
# Return the current local date and time.

from datetime import datetime as dt

print(dt.now()) # 2025-04-19 07:03:10.387253


# 5. Which Year is This?

# The Python documentation for the datetime module provides two attributes to retrieve the year from a 
# date or datetime object: year and isocalendar.

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

# What is the difference between the year attribute and the isocalendar method?

# The difference lies in the fact that the Gregorian year recognises a leap day, 29 February, resulting in 366 days opposed to 365. 
# The ISO year recognises 53 weeks when there is Thursday 1 January and 52 weeks for Wednesday 1 January.
# The week commences on a Monday and ends on a Sunday.


# 6. Argument Signatures

# How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?

# Expects one argument:
# An iterable containing the elements to be joined.


# 7. Find Substring

# Using the official Python documentation, can you determine how to check whether a string contains a specific substring?

str.find(sub[, start[, end]])

# Return the lowest index in the string where substring sub is found within the slice s[start:end]. 
# Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

# Note The find() method should be used only if you need to know the position of sub. 
# To check if sub is a substring or not, use the in operator:

print('Py' in 'Python') # True


# 8. SyntaxError

# The following code raises a SyntaxError:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
# What does a SyntaxError indicate? Try running the above code, then use the resulting error message to fix the error.
# The SyntaxError indidcates that there is syntax missing or inappropriately used. In this case, Python expected : after speed_limit in 
# the if statement. Fixing the syntax is as below:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    

# 9. TypeError

# The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)    # TypeError: can only concatenate str (not "int") to str

# What does a TypeError indicate? 
# Try running the above code, then use the resulting error message to determine exactly what is wrong. 
# (You don't have to fix this code.)

# In the last line of the code, concatenation is attempting to take place prior to the len being determined. Can only concatenate strings with strings.
# Hence, the TypeError is raised as 5 is not a string. If 5 was to be replaced by '5', the TypeError would not occur. 
# Note: '5' has a length of 1 character.
