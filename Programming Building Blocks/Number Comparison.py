one = int(input('First number:  '))
two = int(input('Second number:  '))

if one > two:
    print('The first number is greater than the second.')
else:
    print('The first number is not greater than the second.')

if one == two:
    print('The two numbers are equal.')
else:
    print('The two numbers are not equal.')

if one < two:
    print('The second number is greater than the first.')
else:
    print('The second number is not greater than the first.')

user_animal = input('What is your favorite animal?  ')
user_animal = user_animal.lower()
pro_animal = 'dragon'

if user_animal.find(pro_animal) != -1:
    print('You have chosen well.  Indeed that is my favorite as well.')
else:
    print('Methinks there are better animals to choose as one\'s favorite out there...')
