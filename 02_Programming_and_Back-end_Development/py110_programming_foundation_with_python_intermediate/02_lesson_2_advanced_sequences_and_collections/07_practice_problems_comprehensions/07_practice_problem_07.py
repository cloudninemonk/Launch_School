'''
Given the following data structure return a new list identical in structure to the original, but containing only the numbers that are multiples of 3.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

The returned list should look like this:
[[], [3, 12], [9], [15, 18]]

Try to use a comprehension for this. However, we recommend first trying it without comprehensions.
'''
# ==========
# My Solution
# ==========
# without comprehension
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
new_lst = []

for sublst in lst:
    new_sublst = []
    for num in sublst:
        if num % 3 == 0:
            new_sublst.append(num)
    new_lst.append(new_sublst)

print(new_lst)

#with comprehension
def multiples_of_3(sublst):
    multiples = [num for num in sublst if num % 3 == 0]
    return multiples

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
new_lst = [multiples_of_3(sublst) for sublst in lst]
print(new_lst)


#alternative with comprehension

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
new_lst = [[num for num in sublst if num % 3 == 0] for sublst in lst ]
print(new_lst)

# ==========
# LS Solution
# ==========
# solution 1
new_list = []

for sublist in lst:
    new_sublist = []
    for num in sublist:
        if num % 3 == 0:
            new_sublist.append(num)

    new_list.append(new_sublist)

print(new_list)

# solution 2
new_list = []

for sublist in lst:
    new_sublist = [num for num in sublist if num % 3 == 0]
    new_list.append(new_sublist)

print(new_list)

# solution 3
def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_list = [divisible_by_3(sublist) for sublist in lst]
print(new_list)

# solution 4
new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print(new_list)


