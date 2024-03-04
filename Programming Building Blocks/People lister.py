from os import name


people = [
    'Stephanie 36',
    'John 29',
    'Emily 24',
    'Gretchen 54',
    'Noah 12',
    'Penelope 32',
    'Michael 2',
    'Jacob 10'
]

youngest = []
youngest.append('name')
youngest.append(1999)

for line in people:
    clean_line = line.strip()
    line_list = clean_line.split(" ")
    line_list[1] = int(line_list[1])
    if line_list[1] < youngest[1]:
        youngest[0] = line_list[0]
        youngest[1] = line_list[1]

print(f'As it turns out, the youngest of the list is {youngest[0]} who is {youngest[1]} years old.')
