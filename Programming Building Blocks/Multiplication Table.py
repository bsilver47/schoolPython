table_size = int(input('How many rows and columns would you like?  '))

space_num = len(str((table_size ** 2) + 1))

for i in range(1, table_size + 1):
    for j in range(1, table_size + 1):
        print(f'{i * j:{space_num}}', end = ' ')
    print()
