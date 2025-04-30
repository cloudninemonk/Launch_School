# Assume that obj already has a value of 42 when the code below starts running. 
# Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? Which statements do neither? 
# If necessary, you can read the documentation.


# obj = 'ABcd'          reassign    reassigns a new string to variable obj
# obj.upper()           neither     outputs the UPPERcase of all characters within the string 
# obj = obj.lower()     reassign    reassigns a new string to the variable obj by changing the old string characters to lowercase
# print(len(obj))       neither     outputs the length of the string
# obj = list(obj)       reassign    reassigns the variable type from a string to a list
# obj.pop()             mutate      removes the last element from the list
# obj[2] = 'X'          mutate      reassigns the element at [2] to character 'X' and mutates obj itself
# obj.sort()            mutate      reorders the elements in the list to be in ASCII order
# set(obj)              neither     outputs the list into a set
# obj = tuple(obj)      reassign    reassigns the data type from a set to a tuple