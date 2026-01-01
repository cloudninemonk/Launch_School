'''
The time of day can be represented as the number of minutes before or after midnight. If the number of minutes is positive, the time is after midnight. If the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns the time of day in 24-hour format (hh:mm). Your function should work with any integer input.

You may not use Python's datetime module.

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True
'''

"""
=========================
PEDAC Template
=========================

P: Process the Problem
-------------------------
Input:
- integer

Output:
- string

Rules (Explicit):
- input integer can be +ve or -ve
- -ve integer is in reference to minutes before midnight
- +ve integer is in reference to minutes after midnight

Rules (Implicit/Inferred):
- Seconds are excluded

Mental Model (Optional):
-

E: Examples / Test Cases
-------------------------
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

Edge Cases:
-

D: Data Structures
-------------------------
- str

Notes
-------------------------
-

A: Algorithm (Step-by-step)
-------------------------
1. Pass the integer total_minutes to the function time_of_day
2. Determine the minutes_in_day by multiplying 24 hours by 60 minutes
3. Determine if total_minutes is negative or positive.
4. If negative, subtract total_minutes from minutes_in_day, if not, add total_minutes to 0, and then determine the number of hours and minutes by using divmod
5. Return the string of hours:minutes

C: Code With Intent
-------------------------
"""
# ==========
# My Solution
# ==========
MINUTES_IN_DAY = 24 * 60

def time_of_day(total_minutes):
    while total_minutes < 0:
        total_minutes += MINUTES_IN_DAY # This will ensure that all total_minutes are negative then become positive

    total_minutes = total_minutes % MINUTES_IN_DAY # Only interested in total_minutes < MINUTES_IN_DAY
    hours, minutes = divmod(total_minutes, 60)

    return f'{hours:02d}:{minutes:02d}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# ==========
# LS Solution
# ==========

MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def format_time(hours, minutes):
    return f"{hours:02d}:{minutes:02d}"

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return format_time(hours, minutes)

# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True