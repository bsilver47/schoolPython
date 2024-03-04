name = input ('name? ')
print('hello', name)
print('Want to play a game??')
color = input ('favorite color? ')
# used 'ilver' to account for capitalization discrepencies
silver = ('ilver')
if color.find(silver) != -1:
#if (color = 'silver')
    print (f'{color} is a good choice')
    print (f'{name} is a nice person :)')
else:
    print (f'WRONG: SILVER IS BETTER THAN {color.upper()}')
    print (f'{name} has initiated self-destruct sequence')