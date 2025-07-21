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

You may assume the output will always fit in your terminal window.
"""
# ==========
# My Solution
# ==========
# def print_in_box(text):
#     top_and_bottom = f"+{'-' * (len(text) + 2)}+"
#     above_and_below_text = f"|{' ' * (len(text) + 2)}|"

#     print(top_and_bottom)
#     print(above_and_below_text)
#     print(f"| {text} |")
#     print(above_and_below_text)
#     print(top_and_bottom)


# print_in_box('To boldly go where no one has gone before.')
# print_in_box('')

# # ==========
# # LS Solution
# # ==========
# def print_in_box(message):
#     horizontal_rule = f'+-{"-" * len(message)}-+'
#     empty_line = f'| {" " * len(message)} |'

#     print(horizontal_rule)
#     print(empty_line)
#     print(f'| {message} |')
#     print(empty_line)
#     print(horizontal_rule)

# Further Exploration
# Modify this function so that it truncates the message if it doesn't fit inside
# a maximum width provided as a second argument (the width is the width of the
# box itself). You may assume no maximum if the second argument is omitted.

# For a challenging but fun exercise, try word wrapping messages that are too
# long to fit, so that they appear on multiple lines but are still contained
# within the box. This isn't an easy problem, but it's doable with basic Python.

# ==========
# My Solution
# ==========

# def print_in_box(text, length = 15):
#     top_and_bottom = f"+{'-' * (length - 2)}+"
#     above_and_below_text = f"|{' ' * (length - 2)}|"

#     print(top_and_bottom)
#     print(above_and_below_text)

#     message = ''

#     for i in range(length - 4):
#         message += text[i]

#     print(f"| {message} |")
#     print(above_and_below_text)
#     print(top_and_bottom)

# print_in_box('To boldly go where no one has gone before.')

# def print_in_box(text, length = 15):
#     top_and_bottom = f"+{'-' * (length - 2)}+"
#     above_and_below_text = f"|{' ' * (length - 2)}|"

#     print(top_and_bottom)
#     print(above_and_below_text)

#     message = ''

#     for i in range(len(text)):
#         if (i + 1) % (length - 4) == 0 and i != 0:
#             message += text[i] + ' |\n'
#         elif i % (length - 4) == 0:
#             message += '| ' + text[i]
#         elif i == len(text) - 1:
#             message += text[i] + ' '*((length - 4) - len(text) % (length - 4) + 1) + '|'
#         else:
#             message += text[i]


#     print(message)
#     print(above_and_below_text)
#     print(top_and_bottom)

# print_in_box('To boldly go where no one has gone before.')
# print_in_box('To boldly go where no one has.')

def print_in_box(text, length = 15):
    top_and_bottom = f"+{'-' * (length - 2)}+"
    above_and_below_text = f"|{' ' * (length - 2)}|"

    print(top_and_bottom)
    print(above_and_below_text)

    text_list = text.split()
    current_line = ''

    for word in text_list:
        if len(f"{current_line} {word}") <= length - 4:
            if not current_line:
                current_line = word
            else:
                current_line += f" {word}"

        else:
            print(f"| {current_line}{' '*(length - 3 - len(current_line))}|")
            current_line = word

    print(f"| {current_line}{' '*(length - 3 - len(current_line))}|")
    print(above_and_below_text)
    print(top_and_bottom)

print_in_box('To boldly go where no one has gone before.')
# print_in_box('To boldly go where no one has.')
