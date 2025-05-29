# 8. And on and on and on

# The following code keeps looping forever. (You can hit Ctrl-C to stop it.) Why does the loop keep running? 
# Modify it so that it stops after the first iteration.

# while True:
#     print("and on")


# My response:

# It continues to print "and on" as the print argument "and on" is truthy. While loops instructs Python to print the argument whilst True.

while True:
    print("and on")
    break           # This will terminate the loop after the first iteration.

# An alternative way is to use a counter rather than break.

counter = 1

while counter <= 1:
    print("and on")
    counter += 1

