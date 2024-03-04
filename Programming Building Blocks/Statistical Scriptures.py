with open('books_and_chapters.txt') as scripture_list:
    book = input('Which Volume of scripture would you like to enquire about?  ')
    local_large = ['book', 0, 'scripture']
    grand_large = ['book', 0]
    old_t_size = 0
    new_t_size = 0
    b_o_m_size = 0
    b_o_m_mem = ['book', 0, 'Book of Mormon']
    book_choice = ['book', 0, book]
    choice_min = ['book', 1999, book]
    d_and_c_size = 0
    p_o_g_p_size = 0
    for line in scripture_list:
        line_list = line.strip().split(":")
        line_list[1] = int(line_list[1])
        if line_list[1] > local_large[1]:
            local_large = line_list
        if line_list[2].find('Old Testament') != -1:
            old_t_size += line_list[1]
        elif line_list[2].find('New Testament') != -1:
            new_t_size += line_list[1]
        elif line_list[2].find('Book of Mormon') != -1:
            b_o_m_size += line_list[1]
            if b_o_m_mem[1] < line_list[1]:
                b_o_m_mem[1] = line_list[1]
                b_o_m_mem[0] = line_list[0]
        elif line_list[2].find('Doctrine and Covenants'):
            d_and_c_size += line_list[1]
        else:
            p_o_g_p_size += line_list[1]
        if line_list[2].find(book) != -1:
            if line_list[1] > book_choice[1]:
                book_choice = line_list
            if line_list[1] < choice_min[1]:
                choice_min = line_list
    
    if grand_large[1] < old_t_size:
        grand_large = ['Old Testament', old_t_size]
    if grand_large[1] < new_t_size:
        grand_large = ['New Testament', new_t_size]
    if grand_large[1] < b_o_m_size:
        grand_large = ['Book of Mormon', b_o_m_size]
    if grand_large[1] < d_and_c_size:
        grand_large = ['Doctrine and Covenants', d_and_c_size]
    if grand_large[1] < p_o_g_p_size:
        grand_large = ['Pearl of Great Price', p_o_g_p_size]

    print(f'Did you know, that of the four canonized scriptural texts, {local_large[0]} has the most chapters of any book at {local_large[1]} chapters?')
    print(f'Further, of the canonized texts, the one with the most chapters, at {grand_large[1]}, is The {grand_large[0]}!')
    print(f'To bring things that much further, The longest book in The Book of Mormon is {b_o_m_mem[0]} with {b_o_m_mem[1]} chapters.')
    print(f'Finally, as you requested, the largest book in {book_choice[2]} is {book_choice[0]} with {book_choice[1]} chapters.')
    print(f'Also, for the sake of interest, of the books in {choice_min[2]}, the (first) one with the least chapters is {choice_min[0]} with just {choice_min[1]} chapters.')

