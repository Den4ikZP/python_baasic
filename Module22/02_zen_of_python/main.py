with open('zen.txt') as file:
    print(*[i.strip() for i in file.readlines()[::-1]], sep='\n')
