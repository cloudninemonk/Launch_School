"""
Write a function that takes a year as input and returns the century. The return
value should be a string that begins with the century number, and ends with
'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000
comprise the 20th century.

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
"""

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input: - integer

Output: - string

Rules (Explicit): - returned value is a string containing numbers and letters -
new centuries begin in years that end with 01

Rules (Implicit/Inferred): - Input is an integer

Mental Model (Optional): -

E: Examples / Test Cases
-------------------------
Example 1: - Input: 2000 - Output: "20th"

Example 2: - Input: 2001 - Output: "21st"

Edge Cases: -

D: Data Structures
-------------------------
- strings

Notes
-------------------------
- convert integers to strings

A: Algorithm (Step-by-step)
-------------------------
1. Pass an integer to the function
2. If year <= 100: is the first century
3. If year % 100 == 0: century = str(year / 100) + match/case for the ordinal
   prefix
4. if year % 100 != 0: century = str(year / 100 + 1) + match/case for the
   ordinal prefix

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========

def century(year):
    if year % 100 == 0:
        return str(year // 100) + ordinal_prefix(year // 100)
    if year % 100 != 0:
        return str(year // 100 + 1) + ordinal_prefix(year // 100 + 1)

def ordinal_prefix(century_year):
    if century_year % 100 > 3 and century_year % 100 < 21:
        return 'th'

    match str(century_year)[-1]:
        case '1':
            return 'st'
        case '2':
            return 'nd'
        case '3':
            return 'rd'
        case _:
            return 'th'

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True

