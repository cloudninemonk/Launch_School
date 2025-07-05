# 9. Locale Part 1

"""

Write a function that extracts the language code from a locale. A locale is a combination of a language code, a region, and usually also a character set, e.g en_US.UTF-8.

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

"""

# My response:

def extract_language(locale):
    return locale[0:2]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

# Comments

"""

LSBot recommends making the function more robust by splitting the string at the underscore character and taking the first part, 
as this would handle varying language code lengths.

"""

# Launch School's solution:

"""

def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

"""