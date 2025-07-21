"""Create a simple tip calculator. The program should prompt for a bill amount and a
tip rate. The program must compute the tip, then print both the tip and the total
amount of the bill. You can ignore input validation and assume that the user will
enter valid numbers."""

def calculate_tip(bill, tip):
    """Display the bill and tip amounts."""
    print(f"The bill amount is ${bill:.2f}")
    print(f"The tip amount is ${tip / 100 * bill:.2f}")

bill_amount = float(input("How much is the bill in $? "))
tip_rate = float(input("Enter the tip rate as a %: "))

calculate_tip(bill_amount, tip_rate)
