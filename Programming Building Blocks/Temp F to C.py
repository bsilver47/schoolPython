#input
print('This is to help convert Fahrenheit to Celcius:')
temp = float(input('What is the temperature in Fahrenheit?  '))

#processing
celcius = ((temp - 32) * 5/9)

#output
print(f'The temperature in Celcius is {celcius:.01f}.')