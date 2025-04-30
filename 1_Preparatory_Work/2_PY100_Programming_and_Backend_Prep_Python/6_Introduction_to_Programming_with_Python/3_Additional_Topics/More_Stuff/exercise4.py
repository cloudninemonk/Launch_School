# Write a function called increment_counter that increments a counter variable every time it is called. 
# You can test your code with the following:

# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101


# My response:


# def  increment_counter():
#     counter = 0 
#     counter += 1
#     print(counter)
    
# increment_counter()
# increment_counter()

# Comments:
# I looked at LS's solution prior to solving it myself.
# I experimented with using global and nonlocal but consistently was encounting errors. 


# Launch School's answer:

counter = 0

def increment_counter():
    global counter        # If there was no change to occur to the global variable, would not need to declare global counter.
    counter += 1

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

# In this solution, we've first initialized a global counter variable to 0.
# Our increment_counter function simply incremenets this variable each time the function is called.
# However, since we're using counter += 1 in the code, we need to tell Python that counter, 
# as used in increment_counter, is a global variable. 
# We do this by including global counter in the function definition.