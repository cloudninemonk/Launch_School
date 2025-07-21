"""
Write a function that takes a short line of text and prints it within a box.

Example 1:
    print_in_box('To boldly go where no one has gone before.')

Output for Example 1:
    +--------------------------------------------+
    |                                            |
    | To boldly go where no one has gone before. |
    |                                            |
    +--------------------------------------------+

Example 2:
    print_in_box('')

Output for Example 2:
    +--+
    |  |
    |  |
    |  |
    +--+
"""

def print_in_box(string):
    top_and_bottom = f"+{'-'*(len(string)+2)}+"
    centre_lines = f"|{' '*(len(string)+2)}|"

    print(top_and_bottom)
    print(centre_lines)
    print(f"| {string} |")
    print(centre_lines)
    print(top_and_bottom)

print_in_box('hello world!')
print_in_box('')

""" Limits the box width as per second argument. """
def print_in_box(string, box_width=None):
    """ Default width is None. """
    if box_width is None:
        box_width = len(string) + 2
    top_and_bottom = f"+{'-'* box_width}+"
    centre_lines = f"|{' '* box_width}|"

    print(top_and_bottom)
    print(centre_lines)

    iterator = 0
    truncated_string = ''

    if not string:
        print(f"|{' ' * box_width}|")
    else:
        while iterator < (box_width - 2):
            truncated_string += string[iterator]
            iterator += 1
        print(f"| {truncated_string} |")

    print(centre_lines)
    print(top_and_bottom)

print_in_box('hello world!', 5)
print_in_box('', 5)
