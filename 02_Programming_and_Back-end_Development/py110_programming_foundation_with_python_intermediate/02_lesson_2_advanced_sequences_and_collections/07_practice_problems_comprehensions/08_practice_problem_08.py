'''
Given the following data structure, write some code to return a list that contains the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

The return value should look like this:

[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
'''
# ==========
# My Solution
# ==========

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

# without comprehension

new_lst = []
for item in dict1.values():
    if item['type'] == 'fruit':
        new_lst.append(item['colors'])
    else:
        new_lst.append(item['size'].upper())

print(new_lst)

# with comprehension

def transform_item(item):
    if item['type'] == 'fruit':
        return item['colors']
    else:
        return item['size'].upper()

new_lst = [transform_item(item) for item in dict1.values()]

# ==========
# LS Solution
# ==========
def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result)

