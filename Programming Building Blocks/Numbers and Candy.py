from operator import contains
from tkinter import Y


verify = False

while not verify:
    number = int(input('Please input a number that is positive and whole: '))
    if number >= 0:
        print(f'Great! The number {number} is positive!')
        verify = True
    else:
        print(f'Unfortunately, the number {number} is negative. Please choose a positive number.')

while verify:
    answer = input('Can I please have a cookie? ')
    if (answer.lower()).find('y') != -1:
        verify = False
        print('Thank you!')
