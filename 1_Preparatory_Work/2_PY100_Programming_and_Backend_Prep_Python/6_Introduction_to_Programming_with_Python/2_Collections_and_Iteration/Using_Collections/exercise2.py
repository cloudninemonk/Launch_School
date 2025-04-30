# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

# My response:

text = 'Launch School'
print(text[4:10])


# Launch School's answer:

my_str = 'Launch School'
print(my_str[4:10])                   # ch Sch

# The first c occurs at index 4, so that's our start value for the slice. 
# Since we want 6 characters, the stop value is at index 4 + 6 or 10. 
# Note that the character at index 10 is not included in the result.

# If you want to determine the location of the substring programmatically, you can do this:

my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start:start + 6])        # ch Sch