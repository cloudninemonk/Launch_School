# 8. ATM Withdrawal Simulator
# Simulate withdrawing from a balance. Stop if funds are too low or user exits.

account = 1000
print(f'Your starting balance is {account}')
remaining = account
while remaining > 0:
    withdraw = float(input('How much would you like to withdraw? '))
        
    while withdraw > remaining:
        low_funds_option = input('You do not have enough funds. Would you like to enter another amount? (Y/N)?')
        if low_funds_option == 'Y':
            withdraw = float(input('How much would you like to withdraw? '))
        elif low_funds_option == 'N':
            break
    
    if withdraw > remaining:
        break

    remaining -= withdraw

    if remaining == 0:
        print('You now have no more funds left in your account')
    else:
        print(f'You have ${remaining} remaining in your account.')        
    
    draw_more = input('Would you like to withdraw more cash? (Y/N)? ')
    if draw_more == 'Y':
        continue
    else:
        break


