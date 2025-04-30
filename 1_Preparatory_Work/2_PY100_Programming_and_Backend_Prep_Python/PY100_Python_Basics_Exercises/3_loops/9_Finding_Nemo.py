# 9. Finding Nemo

# Loop over the elements of the fish_list list below, logging each one. 
# Terminate the loop immediately after printing the string 'Nemo'.

# fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']


# My response:

fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)         # Iterates through the fish_list and prints the fish.
    if fish == 'Nemo':  # After each iteration, checks if fish is 'Nemo'
        break           # If fish is 'Nemo', breaks.