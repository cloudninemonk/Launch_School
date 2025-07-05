"""Build a program that asks the user to enter the length and width of a room,
in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet"""

def room_area(length, width):
    "Determines the area of the room in feet and metres squrared"
    length_ft = length * 10.7639
    width_ft = width * 10.7639

    area_m2 = length * width
    print(f"The area of the room is {area_m2:.1f} m^2.")
    area_ft2 = length_ft * width_ft
    print(f"The area of the room is {area_ft2:.1f} ft^2.")

length_metres = float(input("Enter the length of the room in metres: "))
width_metres = float(input("Enter the width of the room in metres: "))

room_area(length_metres, width_metres)
