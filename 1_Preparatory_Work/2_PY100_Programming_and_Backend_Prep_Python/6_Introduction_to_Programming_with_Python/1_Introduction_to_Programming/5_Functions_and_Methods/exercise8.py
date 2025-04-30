# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# My response:

# It will output 42 and 3.141592


# Launch School's answer:

# The code will raise an error:
TypeError: foo() takes 2 positional arguments,
but 3 were given
# We've defined foo with two parameters. However, we've passed the function three arguments. This is an error.


# Comments:

# Similarly to having too few arguments to parameters, you also cannot have
# too many arguments than parameters.
# You have to pass the same number of arguments as the number of positional parameters when invoking functions.