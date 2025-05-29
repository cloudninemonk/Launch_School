my_str = 'bxdxfghi'
count = 0
index = 0

while count < 3:
    if my_str[index] == 'x':
        count += 1
        index += 1
    else:
        index += 1
    
    if index == len(my_str) -1:
        break
    else:
        continue

if count < 3:
    print(None)
else:
    print(f'the third occurrence is {index -1}')