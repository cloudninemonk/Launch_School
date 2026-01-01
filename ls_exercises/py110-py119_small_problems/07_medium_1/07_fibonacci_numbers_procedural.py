'''
The Fibonacci series is a sequence of numbers in which each number is the sum of the previous two numbers. The first two Fibonacci numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth is 1 + 2 = 3, the fifth is 2 + 3 = 5, the sixth is 3 + 5 = 8, and so on. In mathematical terms, this can be represented as:

F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

Write a function called fibonacci that computes the nth Fibonacci number, where nth is an argument passed to the function:

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

If you're familiar with the concept of recursive functions, don't try to write a recursive solution at this time; you'll do that in the next exercise. In other words, write a procedural function that doesn't try to call itself.

If you don't know about or understand recursion, don't worry about it. You'll learn soon enough.

'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integer

Output:
- integer

Rules (Explicit):
- Do not use a recursive function

Rules (Implicit/Inferred):
- Numbers must be integers, i.e., no floats.

Mental Model (Optional):
- Pass an integer to a function. Determine the fibonacci sequence up to that number and return the last number of the fibonacci sequence.

E: Examples / Test Cases
-------------------------
print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

Edge Cases:
-

D: Data Structures
-------------------------
- range: to iterate up to n-2
- list: for storing the fib sequence

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1.
2.
3.

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def fibonacci(num):
    if num > 2:
        fib_seq = [1, 1]
        for _ in range(3, num + 1): # start and stop tied to the fib sequence.
            fib_seq = [fib_seq[-1], fib_seq[-2] + fib_seq[-1]]
        return fib_seq[-1]
    return 1

# ==========
# LS Solution
# ==========

def fibonacci(nth):
    if nth <= 2:
        return 1

    previous, current = 1, 1
    for _ in range(3, nth + 1):
        previous, current = current, previous + current

    return current

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True
