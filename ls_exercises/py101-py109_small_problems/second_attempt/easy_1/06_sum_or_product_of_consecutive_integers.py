"""
Write a program that asks the user to enter an integer greater than 0, then asks
whether the user wants to determine the sum or the product of all numbers
between 1 and the entered integer, inclusive.

Example 1:

Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.

Example 2:

Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
"""

# ==========
# My Solution
# ==========
while True:

    user_number = int(input("Enter an integer greater than 0: "))
    calculation = ''
    while calculation != 's' and calculation != 'p':
        calculation = input(f"Enter 's' to compute the sum, or 'p' to compute thd product of all numbers between 1 and {user_number}: ")

    sum = 0
    product = 1

    for number in range(1, user_number + 1):
        sum += number
        product *= number

    if calculation == 's':
        print(f"The sum of the integers between 1 and {user_number} is {sum}.")
    else:
        print(f"The product of the integers between 1 and {user_number} is {product}.")

    play_again = input("Would you like to play again? ")
    if play_again == 'n':
        break

# ==========
# LS Solution
# ==========

def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
           'or "p" to compute the product: ')

number = int(input(prompt1))
operation = input(prompt2)
print()

if operation == "s":
    print("The sum of the integers between 1 and "
          f"{number} is {compute_sum(number)}.")
elif operation == "p":
    print("The product of the integers between 1 and "
          f"{number} is {compute_product(number)}.")
else:
    print("Oops. Unknown operation.")

# Discussion

# For brevity and simplicity, our solution doesn't try too hard to validate the user input. For completeness, your solution should try to validate input and issue error messages as needed.

# The solution defines two helper functions: compute_sum and compute_product. Which one the program uses depends on the input that is provided by the user ('p' or 's').

# It's worth noting that, for summation, we leverage Python's built-in sum and range functions. Specifically, when using the range function, we provide target_num + 1 as the second argument, since range excludes the end value. This ensures that the target number itself is included in the computation.

# There is no equivalent to sum for computing products built-in to Python, so we have to do so ourselves. Note that the NumPy package does have a prod function, but NumPy is overkill for this exercise.