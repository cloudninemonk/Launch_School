# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)

# My response:

# It will output: 
# 42
# 3.141592
# 2.718


# Launch School's answer:

# The code will print the following:
# 42
# 3.141592
# 2.718 


# Comments:

# As there as many arguments being passed as there are parameters, all arguments 
# will be included despite there being default value parameters for parameter 
# position 2 and 3.

