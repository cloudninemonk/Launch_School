# Write a function that takes a string as an argument and returns an all-caps version 
# of the string when the string is longer than 10 characters. Otherwise, it should 
# return the original string. Example: change 'hello world' to 'HELLO WORLD', but 
# don't change 'goodbye'.


# My response:

def my_str(str):
    if len(str) > 10:
        print(str.upper())
    else:
        print(str)

original_str = input('Enter a string: ')
print(my_str(original_str))


# Launch School's answer:

# def caps_long(string):
#     if len(string) > 10:
#         return string.upper()
#     else:
#         return string

# print(caps_long("Sue Smith"))     # Sue Smith
# print(caps_long("Sue Roberts"))   # SUE ROBERTS
# print(caps_long("Joe Shea"))      # Joe Shea
# print(caps_long("Joe Stevens"))   # JOE STEVENS


# Comments:

# This is another example of where I have answered the question without reading the question properly. The question
# asked for the values to be returned, not printed.