# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# My response:

# An error as return preends no statement. 


# Launch School's answer:

# This code also doesn't print anything. The return on line 3 terminates the function before it can print anything.


# Comments:

# Whilst I was correct that it does not print anything. I was incorrect that it was due to an error occurring. 