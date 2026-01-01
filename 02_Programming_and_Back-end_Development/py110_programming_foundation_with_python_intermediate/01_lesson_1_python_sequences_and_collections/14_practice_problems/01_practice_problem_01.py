'''
How would you count the number of occurrences of "banana" in the following tuple?

fruits = ("apple", "banana", "cherry", "date", "banana")
'''
fruits = ("apple", "banana", "cherry", "date", "banana")

count = fruits.count('banana')
print(count)

# alternatively

count = 0

for fruit in fruits:
    if fruit == 'banana':
        count += 1
print(count)