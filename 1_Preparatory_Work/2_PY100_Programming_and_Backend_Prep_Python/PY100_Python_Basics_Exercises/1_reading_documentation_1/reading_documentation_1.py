# # 1 Finding Documentation
# What is the official place to find Python documentation?

# https://docs.python.org/3/



# # 2 Lowercase
# # Determine whether Python has a method to lowercase a string, for example converting 'Aloha, World!' into 'aloha, world!.

# # It is achievable by using the lower method.

# my_str = 'Hello'
# my_str.lower() # 'hello'



# # 3 Right Justifying Strings
# Use the Python documentation for the str class to determine which method can be used to right justify a str object.
    
# str.rjust(width[, fillchar])
# Return the string right justified in a string of length width. Padding is done using the specified fillchar (default is an ASCII space). 
# The original string is returned if width is less than or equal to len(s).



# # 4 Reverse
# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?
# There is no method to reverse a string, however, there are other ways to do so.
# - Could convert the string to a list and implement the list reverse method, followed by using the join method to convert it back to a string.
# - Could use str[::-1]



# # 5 List Element Access
# How can we access the second element ('and') in the list ['fish', 'and', 'chips']?

# my_list = ['fish', 'and', 'chips']
# my_list[1] # 'and'

# or

# ['fish', 'and', 'chips'][1]



# # 6 Finding Index
# Python lists come with a variety of built-in methods that allow for common list manipulations. 
# One such operation is determining the index of an item in the list.

# Given a list:
# fruits = ["apple", "banana", "cherry", "peach", "watermelon"]

# How would you determine the index of the fruit "cherry" in this list?
# Refer to the official Python documentation on lists to assist with your answer.

# s.index(x[, i[, j]])
# where s is a string

# fruits.index("cherry") # 2



# # 7 Out Of Bounds
# What happens if we take the list ['fish', 'and', 'chips'] and try to access the element at index position 10? 
# First try to determine what will happen by consulting the documentation, then verify your understanding in the Python REPL.

# If index is out of bounds (<0 or >=len(list)), return NULL and set an IndexError exception.

# ['fish', 'and', 'chips'][10]
# # IndexError: list index out of range



# # 8 Large Integers
# Using the Python documentation, determine how you can write large integers in a way that makes them easier to read.

# Underscores are ignored for determining the numeric value of the literal. They can be used to group digits for enhanced readability. 
# One underscore can occur between digits, and after base specifiers like 0x, like so:

# 100_000_000_000

# Is it okay to write 1_987_654_321 as 19_87_65_4321?

# Technically yes but it could be questioned whether it enhances readability as it is not standard convention.
# 1_987_654_321 groups the digits into thousands (1 billion, 987 million, 654 thousand, 321)
# 19_87_65_4321 uses a different grouping (19, 87, 65, 4321), which does not correspond to a standard numerical grouping (e.g., thousands)



# # 9 Checking Data Types
# Referring to the official Python documentation, how would you identify the data type of the following values?

# In Python, everything is an object, and type gives you the class/type of the object.
# The type of a Python object determines what kind of object it is; every object has a type. 
# An object’s type is accessible as its __class__ attribute or can be retrieved with type(obj).

# type(23.5)                  # <class 'float'>

# type('Call me Ishmael.')    # <class 'str'>     

# type(False)                 # <class 'type'>                        
 
# type(0)                     # <class 'int'>

# type(None)                  # <class 'NoneType'>
