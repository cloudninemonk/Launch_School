# Original code resulting in error:
# def calculate(num1, num2, operation):
#     if operation == 'add':
#         return num1 + num2
#     elif operation == 'subtract':
#         return num1 - num2
#     elif operation == 'multiply':
#         return num1 * num2
#     elif operation == 'divide':
#         return num1 / num2
      
# result = calculate(10, 0, 'divide')
# print(f"The result is {result}")
    

# Updated code
def calculate(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
           return 'You cannot have a denominator equal to zero'
    return num1 / num2
      
result = calculate(10, 0, 'divide')
print(f"The result is: {result}")
    