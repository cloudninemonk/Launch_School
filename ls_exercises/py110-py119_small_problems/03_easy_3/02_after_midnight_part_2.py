'''
As seen in the previous exercise, the time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write two functions that each take a time of day in 24 hour format, and return the number of minutes before and after midnight, respectively. Both functions should return a value in the range 0 through 1439.

You may not use Python's datetime module.

Disregard Daylight Savings and Standard Time and other irregularities.

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True
'''
"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- string

Output:
- function return -> integer
- program output -> boolean

Rules (Explicit):
- Not to use datetime module
- two functions: one for before and one for after midnight

Rules (Implicit/Inferred):
- integers are only positive

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

Edge Cases:
-

D: Data Structures
-------------------------
- list

Notes
-------------------------
- split string to obtain the hours and minutes

A: Algorithm (Step-by-step)
-------------------------
1. Pass the time to after_midnight
2. Split the string into hours and minutes
3. Initialise the variables hours and minutes with the integer of the elements within the split string list.
4. return the hours * 60 + minutes
5. before_midnight to return minutes_in_day - after_midnight(time)


C: Code With Intent
-------------------------
"""
MINUTES_IN_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_IN_DAY = HOURS_PER_DAY * MINUTES_IN_HOUR
# ==========
# My Solution
# ==========
def after_midnight(time):
    hours = int(time.split(':')[0])
    minutes = int(time.split(':')[1])
    total_minutes = hours * MINUTES_IN_HOUR + minutes
    return total_minutes % MINUTES_IN_DAY

def before_midnight(time):
    if after_midnight(time) == 0:
        return 0
    return MINUTES_IN_DAY - after_midnight(time)

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# ==========
# LS Solution
# ==========

HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def after_midnight(time_str):
    hours, minutes = [int(unit) for unit in time_str.split(":")]
    return ((hours * MINUTES_PER_HOUR) + minutes) % MINUTES_PER_DAY

def before_midnight(time_str):
    delta_minutes = MINUTES_PER_DAY - after_midnight(time_str)
    if delta_minutes == MINUTES_PER_DAY:
        delta_minutes = 0

    return delta_minutes
