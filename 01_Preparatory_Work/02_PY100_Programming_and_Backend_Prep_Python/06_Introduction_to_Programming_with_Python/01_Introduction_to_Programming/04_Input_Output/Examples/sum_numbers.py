number1 = input('Enter the first number: ') # user input is a string
number2 = input('Enter the second number: ') # user input is a string
sum = number1 + number2 # string concatenation

print(f'The numbers {number1} and {number2} ' 
      f'add to {sum}. #This is a string concatenation') # outputs the string concatenation

# repeat the above exercise to achieve arithmetic sum, NOT string concatentation

sum = float(number1) + float(number2) # arithmetic sum achieved during the variable reassignment

print(f'The numbers {number1} and {number2} ' 
      f'add to {sum} #This is arithmetic sum') # outputs the string concatenation
