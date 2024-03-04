# class_count = int(input('How many classes are you taking?  '))

grade = float(input('What percent did you get?  '))

if grade < 1:
    grade = grade * 100

if grade >= 93:

    letter = 'A'
    succeed = True
elif grade >= 90:

    letter = 'A-'
    succeed = True
elif grade >= 87:

    letter = 'B+'
    succeed = True
elif grade >= 83:

    letter = 'B'
    succeed = True
elif grade >= 80:

    letter = 'B-'
    succeed = True
elif grade >= 77:

    letter = 'C+'
    succeed = True
elif grade >= 73:

    letter = 'C'
    succeed = True
elif grade >= 70:

    letter = 'C-'
    succeed = True
elif grade >= 67:

    letter = 'D+'
    succeed = False
elif grade >= 63:

    letter = 'D'
    succeed = False
elif grade >= 60:

    letter = 'D-'
    succeed = False
else:

    letter = 'F'
    succeed = False


print(f'Your grade is a/an {letter}.')
if succeed == True:
    print(f'You passed!!')
else:
    print(f'I\'m sorry for your lack of passing.')