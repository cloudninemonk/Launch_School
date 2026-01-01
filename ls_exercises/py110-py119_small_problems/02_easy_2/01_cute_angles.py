'''
Write a function that takes a floating point number representing an angle between 0 and 360 degrees and returns a string representing that angle in degrees, minutes, and seconds. You should use a degree symbol (°) to represent degrees, a single quote (') to represent minutes, and a double quote (") to represent seconds. There are 60 minutes in a degree, and 60 seconds in a minute.

Note: You can use the following constant to represent the degree symbol:

DEGREE = "\u00B0"

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- float or integer

Output:
- function return value is an string representing the angle in deg, mins and secs
- program output is a boolean

Rules (Explicit):
- Angle is between 0 and 360 degrees
- 360 degrees can be equal to 0 degrees
- input angle can be an integer or float
- 60 seconds to a minute
- 60 minutes to an angle

Rules (Implicit/Inferred):
-

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
Example 1:
# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")

Edge Cases:
-

D: Data Structures
-------------------------
- int to obtain the integer from a float

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Pass the number to the function dms
2. Initialise three variables:
degrees = int(num)
minutes = int((num - degrees) * 60)
seconds = int(((num - degrees) * 60 - minutes) * 60)
3. Return the string of degrees + minutes + seconds.
Note: Ensure step 3 includes the right formatting for minutes and seconds i.e., a single digit minute or second should be prepended with a '0'

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
DEGREE = "\u00B0"

def dms(num):
    degrees = int(num)
    minutes = int((num - degrees) * 60)
    seconds = int(((num - degrees) * 60 - minutes) * 60)

    return f'{degrees}{DEGREE}{minutes:02}\'{seconds:02}"'

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"" or dms(254.6) == "254°36'00\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")
# Comments:

# Think about whether you want to round to the nearest second instead of always truncating. If you round seconds, you’ll want to handle the carry: secs = round((frac * 60 - minutes) * 60) if secs == 60: secs = 0 minutes += 1 if minutes == 60: minutes = 0 degrees += 1

# ==========
# LS Solution
# ==========
DEGREE = "\u00B0"

def dms(num):
    # Convert to total seconds, rounded to the nearest second
    total_seconds = round(num * 3600)

    # Split into degrees, minutes, seconds
    degrees, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    # If you prefer wrapping 360°00'00" to 0°00'00", uncomment:
    # if degrees == 360 and minutes == 0 and seconds == 0:
    #     degrees = 0

    return f"{degrees}{DEGREE}{minutes:02}'{seconds:02}\""