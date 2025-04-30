# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo() 
print(foo)

# My response:

# The program outputs an error as foo is only scoped to inside the function.


# Launch School's answer:

# The program outputs an error: NameError: name 'foo' is not defined
# Since foo is created inside a function, it isn't in scope when executing code that isn't part of that function.