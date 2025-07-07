"""
What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)
"""

[{"first": "value1"}, {"second": "value2"}, 3, 4, 5]

# ==========
# LS Solution
# ==========

[{'first': 42}, {'second': 'value2'}, 3, 4, 5]

# ==========
# Comments
# ==========

# Refer to the LS Solution for an explanation and revise the theory on shallow and deep copying.