names = []
balances = []
validity = True
total = 0
counter = 0
highest = 0
lowest = 99999999999999999999999999999

while validity:
    name = input('What is this account\'s name?  ')
    if name.find('quit') != -1:
        validity = False
    else:
        balance = float(input('How much money is in this account?  '))
        names.append(name)
        balances.append(balance)
        counter += 1

print('Here is the information for the accounts you just gave:')
for i in range(counter):
    print(f'{i + 1}. {names[i]} - ${balances[i]:.02f}')
    total = total + balances[i]
    if balances[i] > highest:
        highest = balances[i]
        high_name = names[i]
    if balances < lowest:
        lowest = balances[i]
        low_name = names[i]
        

print(f'The total sum of these accounts is ${total:.02f}')
print(f'The average value of these accounts is ${(total / counter):.02f}')
print(f'The account with the most money is {high_name} which holds ${highest:.02f}')
print(f'The account with the least money is {low_name} which holds ${lowest:.02f}')

update = input('Would you like to update an acount? (y/n)  ')
if update.find('y') != -1:
    indexer = int(input('Which account index would you like to update?  '))
    balance = float(input('What is the new value?  '))
else:
    print('Have a nice day!')
