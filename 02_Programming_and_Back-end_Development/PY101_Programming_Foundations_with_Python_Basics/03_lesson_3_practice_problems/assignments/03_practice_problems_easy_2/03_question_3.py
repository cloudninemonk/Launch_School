"""
Programmatically determine whether 42 lies between 10 and 100, inclusive. Do the
same for the values 100 and 101.
"""

numbers = list(range(10,101))
target = [42, 100, 101]

for number in target:
    if number in numbers:
        print(f"{number} lies between 10 and 100, inclusive. ")
    else:
        print(f"{number} does not lie between 10 and 100, inclusive. ")

# No need to construct a list. Can check against range directly. i.e., number in
# range(10,101)
"""
LS Solution
"""

42 in range(10, 101)          # True
100 in range(10, 101)         # True
101 in range(10, 101)         # False
