import random
text = open("Wordle Words.txt")
text_list = text.readlines()

def main():
    numbers = [16.2, 75.1, 52.3, 47.9]
    print(numbers)
    
    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    words_list = []
    number = random.randint(1,10)

    append_random_words(words_list)
    print(words_list)

    append_random_words(words_list, 3)
    print(words_list)


def append_random_numbers(numbers, quantity=1):
    for i in range(quantity):
        num = round(random.uniform(0, 100), 1)
        numbers.append(num)
    return numbers

def append_random_words(words_list, quantity=1):
    for i in range(quantity):
        number = random.randint(1,1163)
        wordle = text_list[number]
        words_list.append(wordle)
    return words_list


if __name__ == "__main__":
    main()


text.close()