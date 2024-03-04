import math
e = math.e

mass = float(input('Mass (kg):  '))
gravity = float(input('Gravitational acceleration (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter, 11.22 m/s^2 on Proxima B):  '))
time = float(input('Time in seconds:  '))
density = float(input('Density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water):  '))
area = float(input('Cross sectional area of projectile (in square meters):  '))
drag = float(input('Drag constant (0.5 for a sphere, 1.1 for a cylinder on it\'s side, 0.8 for a cube, 0.4 for a bird, 1.8 for a motorcycle and rider):  '))

c = (density * area * drag / 2)
velocity = (math.sqrt(mass * gravity / c) * (1- e ** (-1 * time * (math.sqrt(mass * gravity * c) / mass))))
v_terminal = (math.sqrt(mass * gravity / c))


print(f'The inner value of c is: {c:.03f}')
if (v_terminal <= velocity):
    print(f"The given object has attained terminal velocity.  The speed of the object at {time} is: {v_terminal:.03f}")
else:
    print(f'The velocity that given object would obtain after {time} seconds is: {velocity:.03f}')