"""
Back in the stone age (before CSS), we used spaces to align things on the
screen. If we have a 40-character wide table of Flintstone family members, how
can we center the following title above the table with spaces?

title = "Flintstone Family Members"
"""

title = "Flintstone Family Members"
table_width = 40
spaces_on_side = (table_width - len(title)) // 2 * ' '


if spaces_on_side % 2 != 0:
    print(spaces_on_side + title + spaces_on_side + 1)
else:
    print(spaces_on_side + title + spaces_on_side)

# ==========
# LS Solution
# ==========

centered_title = title.center(40)

# ==========
# This is a reminder to refer to the Python documentation if the way
# I am coding seems cumbersome to achieving the desired result.
# ==========

