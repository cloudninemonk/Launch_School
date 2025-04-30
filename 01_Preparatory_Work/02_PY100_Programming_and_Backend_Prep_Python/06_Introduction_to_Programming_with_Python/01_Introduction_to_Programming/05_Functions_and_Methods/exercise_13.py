# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# My response:

# It will print result in an error as there is no default value declared for 
# position 3 parameter within foo.


# Launch School's answer:

# The code will raise an error:

# SyntaxError: non-default argument follows
# default argument

# Here, we've defined foo with three parameters, with the second parameter 
# having a default value. This is an error, however. Once Python sees a 
# positional parameter with a default value, all subsequent parameters must 
# have default values.


# Comments:
# Whereever the first default value is declared, all subsequent parameters are to include
# default values otherwise the code will output an error when run.