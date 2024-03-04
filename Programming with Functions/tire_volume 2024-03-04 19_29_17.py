import math
from datetime import date

verify = True
pi = math.pi
current_date = date.today()

print(f"Today is {current_date}.")

def volume(width, aspect_ratio, diameter):
    vol = ((pi * width * width * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000)
    return vol

def main(volumes_file, verify):
    width = int(input("What is the width of the tire? "))
    aspect_ratio = int(input("What is the aspect ratio of the tire? "))
    diameter = int(input("What is the diameter of the tire? "))

    vol = round(volume(width, aspect_ratio, diameter), 2)
    print(f"The volume of the tire is {vol} Liters.\n")
    print(current_date, width, aspect_ratio, diameter, vol, sep=', ', end='\n', file=volumes_file, flush=False)

    ending = input("Would you like to add more tires to the list? ('Y' if yes) ").lower()
    if ending.find('y') != -1:
        print("Very well!")
        verify = True
    else:
        verify = False
        print('Then have a great day! Please remember to access your saved data in the file "volumes.txt"')
    return verify

with open("volumes.txt", mode="at") as volumes_file:
    while verify:
        verify = main(volumes_file, verify)
