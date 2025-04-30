# Consider the following code:

# def sum_of_squares(num1, num2):
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# Write a nested function in sum_of_squares that will make this code work as shown.


# My response:

def sum_of_squares(num1, num2):
    def square(num):
        return num**2
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)


# Launch School's answer:

def sum_of_squares(num1, num2):
    def square(number):
        return number * number

    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# In this solution, we've added a nested function to calculate the square of the number passed to it as an argument. 
# Assuming we don't need square anyplace else in our code, we can nest it inside sum_of_squares to help keep the global scope "clean"; 
# that is, the global scope doesn't include anything that isn't used by the top-level code.