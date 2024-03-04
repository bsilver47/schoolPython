with open('books.txt') as text_file:
    for line in text_file:
        clean_line = line.strip()
        print(f'{clean_line}')
        a