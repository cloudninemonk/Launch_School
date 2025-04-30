# Use the sqrt function from the math library to write some code that outputs the square root of 37. 
# Try to write the code in three different ways.

# My response:

import math

def my_sqrt(my_num):
        print(math.sqrt(my_num))

my_sqrt(37) 


from math import sqrt

def my_sqrt(my_num):
        print(sqrt(my_num))

my_sqrt(37) 


import math as m

def my_sqrt(my_num):
        print(m.sqrt(my_num))

my_sqrt(37) 


# Launch School's answer:

# Using the import statement
import math

print(math.sqrt(37))         # 6.082762530298219

# Using an import alias
import math as m

print(m.sqrt(37))            # 6.082762530298219

# Using the from statement
from math import sqrt

print(sqrt(37))              # 6.082762530298219