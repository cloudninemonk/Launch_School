# 5. Display Division

"""

Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three

"""

# My response:

"""

# 3 / 1 = 3
# 6 / 2 = 3
# 9 / 3 = 3
# 12 / 4 = 3
# 15 / 5 = 3
# 18 / 6 = 3
# 21 / 7 = 3
# 24 / 8 = 3
# 27 / 9 = 3
# 30 / 10 = 3

"""

# Launch School solution:

"""

There will be no output since the function multiples_of_three is never invoked.

If you used a REPL to run this code, you may have seen a return value that looks something like this:

<function multiples_of_three at 0x102656200>

Note that return values are not outputs. That you see them at all is solely an implementation detail of your REPL.
 
"""