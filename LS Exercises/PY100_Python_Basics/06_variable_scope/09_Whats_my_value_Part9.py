# 9. What's my value? (Part 9)

"""

What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

"""

# My response:

"""

The code will output 7 as the global variable a is unchanged despite what the function,
my_function, performs.

"""

# Comments:

"""

My solution is fundamentally correct, but I could enhance it by explaining why the variable 
remains unchanged. Consider mentioning Python's pass-by-value behavior for immutable types like 
integers, and explaining that when b += 10 is executed, it creates a new object rather than 
modifying the original one. This would demonstrate a deeper understanding of Python's memory 
model and how immutable objects behave when passed to functions.

For example, I could elaborate: "In Python, integers are immutable. When a is passed to the 
function as argument b, any operation on b creates a new object rather than modifying the original. 
So b += 10 creates a new integer object with value 17, but this doesn't affect the original variable 
a in the global scope."

"""