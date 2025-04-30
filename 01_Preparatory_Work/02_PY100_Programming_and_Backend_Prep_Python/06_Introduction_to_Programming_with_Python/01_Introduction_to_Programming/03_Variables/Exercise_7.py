#What happens when you run the following code? Why?

# greets Victor 3 times
NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# greets Nina 3 times
NAME = 'Nina'           
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# The reassignment of the constant NAME is not good practice, however, 
# Python does not have true constants so this rule can be broken.
# If you wanted to change the name of Victor to the name of Nina, should declare the variable NAME as name,
# i.e. lowercase