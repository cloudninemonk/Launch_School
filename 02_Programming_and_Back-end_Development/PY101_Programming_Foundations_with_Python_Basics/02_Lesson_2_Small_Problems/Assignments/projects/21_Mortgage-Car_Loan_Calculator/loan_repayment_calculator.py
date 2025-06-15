'''This is a program that determines the monthly repayments on a loan'''


def repayment(loan, rate, duration):
    '''This function determines the monthly interest rate and duration of loan in months based on the user input of annual
    interest rate and number of years for the loan duration. It then determines the monthly repayment amount.'''

    rate_mthly = rate / 12 / 100
    duration_mths = duration * 12

    if rate_mthly == 0:
        return loan/ duration_mths
    return loan * (rate_mthly / (1 - (1 + rate_mthly) ** (-duration_mths)))

while True:
    while True:
        try:
            loan_amount = float(input("Enter a loan amount in dollars ($): "))
            if loan_amount <=0:
                print("Enter an amount greater than zero. ")
            break
        except ValueError:
            print("The loan amount you entered is not valid.")

    while True:
        try:
            interest_rate = float(input("What is the annual interest rate as a percentage(%)? "))
            if interest_rate <  0:
                print("Enter a rate of zero or greater. ")
            else:
                break
        except ValueError:
            print("The rate you entered is not valid.")

    while True:
        try:
            loan_duration = float(input("What is the duration of the loan in years? "))
            if loan_duration <= 0:
                print("Enter a duration greater than zero. ")
            else:
                break
        except ValueError:
            print("The duration you entered is not valid.")

    monthly_repayment = repayment(loan_amount, interest_rate, loan_duration)
    rounded_repayment = ((monthly_repayment * 100) - (monthly_repayment * 100 % 1)) / 100

    print(f'The monthly repayment on your loan is ${rounded_repayment}')
    print(f'''The total repayment on ${loan_amount} over {int(loan_duration)} years is:
${rounded_repayment * 12 * loan_duration}''')

    answer = input("Would you like to perform another calculation? ").lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break
        answer = input("Please enter 'y' or 'n'.".lower())

    if answer[0] == 'n':
        break

