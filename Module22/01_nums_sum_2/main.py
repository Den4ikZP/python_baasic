with open('numbers.txt') as file, open('answer.txt', 'w') as answer:
    answer.write(str(sum([int(i.strip()) for i in file.readlines()])))
