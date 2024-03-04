height1 = float(input('What is the height of the first rider (in inches)?  '))
age1 = int(input('What is the age of the first rider (in years)?  '))
if age1 >= 12 and age1 <= 17:
    golden1 = input('Do you have a Golden Passport?(Yes/No)  ').lower()
    if golden1.find('yes') != -1:
        age1 = 18

another = input('Is there another rider?(Yes/No)  ').lower()
if another.find('yes') != -1:
    height2 = float(input('What is the height of the second rider (in inches)?  '))
    age2 = int(input('What is the age of the second rider (in years)?  '))
    if age1 >= 12 and age1 <= 17:
        golden2 = input('Does the second rider have a Golden Passport?(Yes/No)  ').lower()
        if golden2.find('yes') != -1:
            age2 = 18
    if height1 < 36 or height2 < 36:
        eligible = False
    else:
        if (age1 > 17 or age2 > 17):
            eligible = True
        elif age1 > 11 and age2 > 11:
            if height1 > 51 and height2 > 51:
                eligible = True
        elif age1 >= 16 and age2 >= 14:
            eligible = True
        elif age1 >= 14 and age2 >= 16:
            eligible = True
        else:
            eligible = False
else:
    if height1 < 36:
        eligible = False
    else:
        if age1 > 17:
            eligible = True
        else:
            eligible = False
if eligible:
    print('Please keep your hands, arms feet and legs inside the vehicle and have fun!')
    print('¡Por favor, entenga las manos, brazos, pies, y piernas dentro del vehiculo y que se divierta!')
else:
    print('We apologize for the inconvenience, you cannot ride at this time.')