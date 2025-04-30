# Don't let the math scare you. This is a logic and syntax problem, not a math problem.
# Write a function that computes and returns the factorial of a number by using a for or while loop. 
# The factorial of a positive integer n, signified by n!, is defined as the product of all integers between 1 and n, inclusive:

# n!	Expansion	        Result
# 1!	1	                1
# 2!	1 * 2	            2
# 3!	1 * 2 * 3	        6
# 4!	1 * 2 * 3 * 4	    24
# 5!	1 * 2 * 3 * 4 * 5	120

# You may assume that the argument is always a positive integer.

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000

# My response:

def factorial(n):
    result = 1
    for number in range(n):
        result = result * (i+1)
    return result

n = int(input('Enter an integer: '))
print(f'The factorial for the integer you entered is: {factorial(n)}')

# Comments:
# LS incorporate a range that stepped backwards from the given argument n. 
# LS utilised augmented assignment to make the code cleaner.
# LS incorporate a space between the end of the for loop and the return statement


# Launch School's answer:

# while loop

def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

    return result

# Our first solution uses a while loop to compute the return value. We begin by assigning the result variable to 1, 
# then we multiply result by all of the integers between n and 1, inclusive. 
# Note that we need to decrement n by 1 at the end of each iteration.

# for loop

def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

# The second solution is similar, but it uses a for loop instead of a while loop. 
# The benefit of using for is that we don't need to worry about decrementing n. 
# Instead, we just iterate over the integers between n and 1, inclusive, using a range.

