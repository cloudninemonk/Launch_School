'''
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
'''
# When trying to access the value assigned to 'b' using key accessing, an error arises if the key does not exist. Better to use the dict.get method which returns None if the key does not exist. In this instance the if statement will evaluate whether my_dict.get('b') if truthy, which it is not as my_dict.get('b') returns None and None is falsy.

# solution 1
def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# solution 2
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))

# ==========
# LS Solution
# ==========
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

# note: LS Solution includes a default value for the get method to return. In this instance, None is redundant as the get method returns None if the key does not exist.