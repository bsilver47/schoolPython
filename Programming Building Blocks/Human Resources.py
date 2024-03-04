with open('hr_system.txt') as text_file:
    for line in text_file:
        clean_line = line.strip()
        line_list = clean_line.split(" ")
        line_list[3] = float(line_list[3])
        line_list[3] = line_list[3] / 24
        if line_list[2].find("Engineer") != -1:
            line_list[3] += 1000
        print(f'Name: {line_list[0]}, (ID: {line_list[1]}) Title: {line_list[2]} - ${line_list[3]:.02f}')
        