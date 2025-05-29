# Original code
# def count_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0 
      
#     for char in string:
#         if char in vowels:
#           count + 1 # this is an expression that is not assigned to any variable.
      
#     return count
      
# text = "Hello World"
# print(f"The text '{text}' has {count_vowels(text)} vowels.")

# Updated code

def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count

text = "Hello World"
print(f"The text '{text}' has {count_vowels(text)} vowels.")