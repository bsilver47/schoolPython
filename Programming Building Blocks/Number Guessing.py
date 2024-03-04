import random

reattempt = True
highscore = 1000000

while reattempt:
    number = random.randint(1,100)
    counter = 1
    #print(f'{number}')

    guess = int(input('What would you guess the random number is?  '))

    while number != guess:
        if number > guess:
            print('Higher')
            counter += 1
            guess = int(input('What would you guess the random number is?  '))
        else:
            print('Lower')
            counter += 1
            guess = int(input('What would you guess the random number is?  '))

    print('You win!')
    print(f'It took you {counter} tries.')
    if counter < highscore:
        highscore = counter
        print('New High Score!')
    retry = input('Want to play again?  ').lower()
    if retry.find('yes') == -1:
        reattempt = False

print('Thank you for playing!')
print(f'Ultimate High Score:  {highscore}')
print('Have a nice day!  :)')
