'''
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
'''
# ==========
# My Solution
# ==========
def invert_dict(dict1):
    return {value: key for key, value in dict1.items()}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# ==========
# LS Solution
# ==========

def invert_dict(my_dict):
    return {value: key for key, value in my_dict.items()}