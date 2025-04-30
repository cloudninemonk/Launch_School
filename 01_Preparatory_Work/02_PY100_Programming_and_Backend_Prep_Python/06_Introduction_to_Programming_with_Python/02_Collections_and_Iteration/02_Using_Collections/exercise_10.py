# Consider the following nested collection:

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

# Write one line of code to print the activities that Cocoa enjoys.

# My response:

# Was stuck on this one and hence did not produce an answer.


# Launch School's answer:

print(cats['Pete']['Cocoa']['enjoys'])
