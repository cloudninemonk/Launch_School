# 6. Check the Weather, Part 2

# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement. 
# Feel free to add more cases besides 'sunny' and 'rainy'.


# My response:

weather = 'hailing'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case _:
        print("Let's stay inside.")