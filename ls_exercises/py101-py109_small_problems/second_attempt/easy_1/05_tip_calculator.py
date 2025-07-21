"""
Create a simple tip calculator. The program should prompt for a bill amount and
a tip rate. The program must compute the tip, then print both the tip and the
total amount of the bill. You can ignore input validation and assume that the
user will enter valid numbers.

What is the bill? 200
What is the tip percentage? 20

The tip is $40.00
The total is $240.00
"""

# ==========
# My Solution
# ==========

bill_amount = float(input("How much is the bill ($)? "))
tip_percentage = float(input("How much would you like to tip (%)? "))

tip_amount = bill_amount * (tip_percentage / 100)

print(f"The tip is ${tip_amount:.2f}")
print(f"The total is ${(bill_amount + tip_amount):.2f}")

# ==========
# LS Solution
# ==========

# bill = float(input("What is the bill? "))
# percentage = float(input("What is the tip percentage? "))

# tip = bill * (percentage / 100)
# total = bill + tip

# print(f"The tip is ${tip:.2f}")
# print(f"The total is ${total:.2f}")
