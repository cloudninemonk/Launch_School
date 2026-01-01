'''
Given two lists of integers of the same length, return a new list where each element is the product of the corresponding elements from the two lists.

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True
'''
# ==========
# My Solution
# ==========
def multiply_items(list1, list2):
    return [list1[idx] * list2[idx] for idx in range(len(list1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# ==========
# LS Solution
# ==========
#solution 1
def multiply_items(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i] * list2[i])

    return result

# solution 2
def multiply_items(list1, list2):
    return [num1 * num2 for num1, num2 in zip(list1, list2)]