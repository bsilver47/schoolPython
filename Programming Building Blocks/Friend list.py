friend_list = []

friend_count = int(input('How many friends do you have?  '))

for x in range(friend_count):
    ind_friend = input(f'What is the name of friend {x + 1}?  ')
    if ind_friend.find('end') != -1:
        break
    friend_list.append(ind_friend)

for friend in friend_list:
    print(f'{friend} is now registered as a friend')
