print('We will ask you a series of questions.  We ask that you respond on a scale from 1 to 10')
loan_size = int(input('How big is the loan?  '))
credit_history = int(input('How\'s your credit?  '))
income = int(input('How\'s your income?  '))
down_payment = int(input('How big is your down payment?  '))

if loan_size >= 5:
    if income >= 7 and credit_history >= 7:
        qualify = True
    elif income >= 7 or credit_history >= 7:
        if down_payment >= 5:
            qualify = True
        else:
            qualify = False
    else:
        qualify = False
else:
    if credit_history < 4:
        qualify = False
    elif income >= 7 or down_payment >= 7:
        qualify = True
    elif income >= 4 and down_payment >= 4:
        qualify = True
    else:
        qualify = False

if qualify:
    print('Yes, you do qualify for your loan.')
else:
    print('No, unfortunately you do not qualify for your loan.')
        