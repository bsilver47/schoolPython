import math
pi = math.pi

#Area of a square
square_side = float(input('Side length of the square in centimeters:  '))
print(f'The area of the square is {square_side ** 2} cm^2 or {(square_side / 100) ** 2} m^2.')

#area of a rectangle
rect_length = float(input('Length of the rectangle in centimeters:  '))
rect_width = float(input('Width of the rectangle in centimeters:  '))
print(f'The area of the rectangle is {rect_length * rect_width} cm^2 or \
{(rect_length * rect_width) / 10000} m^2.')

#area of a circle
radius = float(input('Radius of the circle in centimeters:  '))
print(f'The area of the circle is {pi * (radius ** 2)} cm^2 or \
{(pi * (radius ** 2)) / 10000} m^2.')

#stretch exercize
length = float(input('Please give a single length value:  '))
print(f'For {length} length, you would have a square with an area of {length ** 2}, \
a circle with an area of {pi * (length ** 2)}, a cube with a volume of {length ** 3}, \
and a sphere with a volume of {(4/3) * pi * (length ** 3)}.')