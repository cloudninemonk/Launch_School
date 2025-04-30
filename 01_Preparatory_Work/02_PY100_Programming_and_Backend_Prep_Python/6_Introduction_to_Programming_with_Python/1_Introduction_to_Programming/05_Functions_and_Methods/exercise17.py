# Which of the identifiers in the following program are function names? 
# Which are method names? Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))


# My response:

# Function names:
# say, print (built-in), input (built-in), max (built-in)

# Method names:
# upper, lower


# Launch School's answer:

# Function Names	Method Names	Built-in Function Names
# say		
#                                   print
#                                   input
#                                   max
#                   upper	
#                   lower	

# If you identified all the method and built-in function names as function names, 
# that's an acceptable answer as well: all methods are functions, and built-in 
# functions are just functions that are, well, built-in.