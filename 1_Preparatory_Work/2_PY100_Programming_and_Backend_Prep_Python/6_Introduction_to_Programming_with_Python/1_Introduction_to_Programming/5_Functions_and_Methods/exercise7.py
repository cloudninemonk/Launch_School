# Without running the following code, what do you think it will do?

def foo(bar, text = 'qux'):
    print(bar)
    print(text)

foo('Hello')

# My response:

# It will print Hello and then output an error.


# Launch School's answer:

# The code will raise an error:
# TypeError: foo() missing 1 required positional
# argument: 'qux'


# Comments:

# A function requires the same number of arguments as the function has parameters,
# unless you declare default parameters within the function.