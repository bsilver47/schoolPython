def main(): 
    #introduction
    print("Let's have some fun!")
    print("Please enter a word for each of the following word types:")

    #input
    noun1 = input('unit of time:  ')
    number1 = input('number greater than 1:  ')
    noun2 = input('plural noun:  ')
    noun3 = input('noun:  ')
    adjective1 = input('adjective:  ')
    noun4 = input('noun:  ')
    emotion1 = input('emotion:  ')

    #processing
    article3 = article(noun1)
    article1 = article(noun3)
    article2 = article(adjective1)

    #output
    print(f'''
    Once upon {article3} {noun1}, there were {number1} {noun2} that lived\r\n\
    in {article1} {noun3} until one day, {article2} {adjective1} {noun4} came.\n\
    This caused the {noun2} to be very {emotion1}.  As such,\n\
    the {number1} {noun2} decided to peacefully move to an even\n\
    larger {noun3} to live out the remainder of their {noun1}.
    ''')
    print(f"")

#function to help maintain grammer in mad lib
def article(word):
    vowel = 'aeiou'
    if word[0].lower() in vowel:
        return 'an'
    else:
        return 'a'

#excecution of code
main()
