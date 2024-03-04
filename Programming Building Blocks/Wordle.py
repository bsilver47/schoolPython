import random
##path = "C:\Users\Benjamin Silver\Desktop\Programming Building Blocks\Wordle Words.txt"
##Wordle Words was a txt file that I created using the following two webpages:
##https://www.thefreedictionary.com/5-letter-words.htm
##https://7esl.com/5-letter-words/R

##with open('Wordle Words.txt', 'r') as text_file:
##text_file = open(path, 'r')
text = open('Wordle Words.txt')
##text = text_file.read()
##text_list = text.split('\n')
text_list = text.readlines()

reattempt = True
counter = 1

while reattempt:
    number = random.randint(1,1163)
    wordle = text_list[number].read()
    print(wordle)
    hint = ' _ _ _ _ _'

    for i in range(5):
        guess = (input('What would you guess the five letter word is? '))
        if guess == wordle:
            print('You win!')
            break
        else:
            for i in wordle:
                for j in guess:
                    if wordle[i] == guess[j]:
                        hint[(i + 1)] = wordle[i]
            counter += 1
            print(f'Not quite, but you did get this right:')
            print(hint)

    print(f'It took you {counter} tries.')
    
    retry = input('Want to play again?  ').lower()
    if retry.find('yes') == -1:
        reattempt = False

print('Thank you for playing!')
print('Have a nice day!  :)')
text.close()