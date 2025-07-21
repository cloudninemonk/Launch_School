"""
Build a program that asks the user to enter the length and width of a room, in
meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet
"""

# ==========
# My Solution
# ==========


length = float(input("Enter the length of the room in metres: "))
width = float(input("Enter the width of the room in metres: "))

room_area_metres = length * width
room_area_feet = room_area_metres * 10.7639

print(f"The area of the room in m2 is: {room_area_metres:.2f}")
print(f"The area of the room in ft2 is: {room_area_feet:.2f}")

# ==========
# Further Exploration
# ==========

length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
units = input("What units are your dimensions in, feet or metres (ft or m)? ")

room_area_metres = length * width
room_area_feet = room_area_metres * 10.7639

if units == 'm':
    print(f"The area of the room is: {room_area_metres:.2f} m2 ({room_area_feet:.2f} ft2)")
else:
    print(f"The area of the room is: {room_area_feet:.2f} ft2 ({room_area_metres:.2f} m2)")

# ==========
# LS Solution
# ==========

# length = float(input("Enter the length of the room in meters: "))
# width = float(input("Enter the width of the room in meters: "))

# area_in_meters = length * width
# area_in_feet = area_in_meters * 10.7639

# print(f"The area of the room is {area_in_meters:.2f} "
#       f"square meters ({area_in_feet:.2f} square feet).")

# Discussion

# Our approach is straightforward. The program first collects input values for
# the length and width of a room, performs the necessary computations to
# determine the area, then displays the results. This solution does not check
# for invalid user input.

# Some key things to note:

# The input function returns a string. Thus, we need to use the float function
# to convert this string to a floating-point number. The format specification
# {:.2f} ensures that the output is formatted to two decimal places.
#
# Further Exploration
#
# Modify the program to let the user specify the measurement type
# (meters or feet). Compute the area accordingly and print it and its conversion
# in parentheses.

