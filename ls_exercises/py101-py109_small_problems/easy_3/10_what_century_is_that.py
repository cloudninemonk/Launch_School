"""
Write a function that takes a year as input and returns the century. The return
value should be a string that begins with the century number, and ends with
'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000
comprise the 20th century.

Examples:
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

def century(year):
    cardinal_number = year // 100
    if year <= 100:
        return "1st"
    if year % 1000 == 0:
        return f"{cardinal_number}th"
    if year % 100 == 0:
        suffix = ordinal_suffix(cardinal_number, year)
        return f"{cardinal_number}{suffix}"
    if year % 100 != 0:
        suffix = ordinal_suffix(cardinal_number, year)
        return f"{cardinal_number + 1}{suffix}"

def ordinal_suffix(cardinal_number, year):
    if (cardinal_number % 100) // 10 == 1:
        return 'th'
    else:
        match (cardinal_number + 1) % 10:
            case 1:
                return 'st'
            case 2:
                return 'nd'
            case 3:
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