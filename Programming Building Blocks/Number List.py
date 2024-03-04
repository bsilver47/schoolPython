num_list = []
number = -1
counter = -1
print('Here is your opportunity to give a list of numbers!  Please enter 0 as the number to indicate that your list is complete.')
while number != 0:
    number = int(input('Number:  '))
    num_list.append(number)
    counter += 1

print('Thank you for participating!')
print('Please hold while I work with the list you gave me!')

#sum
sum_total = 0
for num in num_list:
    sum_total += num

#average
avg = round(sum_total / counter)
#avg = round(avg)

#largest number
big = 0
for num in num_list:
    if num > big:
        big = num

#find the smallest positive integer
positive = 100000
for num in num_list:
    if (num > 0) and (num < positive):
            positive = num

#organize the list to go from smallest to largest

num_list.sort()

print('Assuming that I am correct:  ')
print(f'The sum of your numbers is {sum_total}')
print(f'The average of your numbers is {avg}')
print(f'The largest of your numbers is {big}')
print(f'Of your positive numbers, the smallest is {positive}')
print('The following is your list reorganized from lowest to highest:')
print(*num_list, sep='\n')
