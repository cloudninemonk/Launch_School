# Without running the following code, what does it print? Why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)


# My response:

# Product2
# Product3


# Launch School's answer:

# Product2
# Product not found! # As the argument 142 is an integer and the case '142' is a string.

# The first call to bar_code_scanner prints Product2 since the first case that matches '113' is the one on line 5. 
# The second call prints Product not found! since the numeric value 142 doesn't match any of the case statements 
# with string arguments. Instead, it matches the _ "default" case.


# Comments:
# Important for me to read the question and the code carefully before providing an answer. 
# Do the due diligence of double checking my answers every time. 