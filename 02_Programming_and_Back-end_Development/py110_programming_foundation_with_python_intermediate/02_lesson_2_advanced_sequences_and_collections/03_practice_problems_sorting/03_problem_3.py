'''
Repeat problem 2 but, this time, sort the list as string values. Both the list passed to the sorting function and the returned list should contain numbers, not strings.

lst = [10, 9, -6, 11, 7, -16, 50, 8]
'''

lst = [10, 9, -6, 11, 7, -16, 50, 8]

ascending_lst = lst.sort(key=str)
descending_lst = lst.sort(key=str, reverse=True)
