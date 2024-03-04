with open('life-expectancy.csv') as life_list:
    interest = int(input('What year would you like to know about?  '))
    lowest_life = [4]
    highest_life = [4]
    year_lowest = [4]
    year_highest = [4]
    lowest_life[0] = 'country'
    highest_life[0] = 'country'
    lowest_life.append('code')
    highest_life.append('code')
    lowest_life.append(2000)
    highest_life.append(1999)
    lowest_life.append(300.0)
    highest_life.append(0.0)
    year_lowest[0] = 'country'
    year_highest[0] = 'country'
    year_lowest.append('code')
    year_highest.append('code')
    year_lowest.append(2000)
    year_highest.append(1999)
    year_lowest.append(300.0)
    year_highest.append(0.0)
    year_average = 0
    counter = 0
    coder_year = ['country', 'code', 1999, 0.0]

    header = next(life_list)
    for line in life_list:
        clean_line = line.strip()
        line_list = clean_line.split(",")
        line_list[2] = int(line_list[2])
        line_list[3] = float(line_list[3])
        if line_list[3] > highest_life[3]:
            highest_life = line_list
        if line_list[3] < lowest_life[3]:
            lowest_life = line_list
        if line_list[2] == interest:
            year_average += line_list[3]
            counter += 1
            if line_list[3] > year_highest[3]:
                year_highest = line_list
            if line_list[3] < year_lowest[3]:
                year_lowest = line_list
        if line_list[2] == coder_year[2]:
            if line_list[3] > coder_year[3]:
                coder_year = line_list
    
    year_average = year_average / counter

    print(f'Overall, the record for the highest life expectancy was {highest_life[3]} in {highest_life[0]} in {highest_life[2]}.')
    print(f'Overall, the record for the lowest life expectancy was {lowest_life[3]} in {lowest_life[0]} in {lowest_life[2]}.')
    print(f'In {interest}:')
    print(f'Globally, the life expectancy was {year_average:.02f}.')
    print(f'As it happens, the greatest life expectancy was {year_highest[3]} in {year_highest[0]}.')
    print(f'As it happens, the greatest life expectancy was {year_lowest[3]} in {year_lowest[0]}.')
    print(f'Also, the highest life expectancy in 1999 was {coder_year[3]:.02f} in {coder_year[0]}.')