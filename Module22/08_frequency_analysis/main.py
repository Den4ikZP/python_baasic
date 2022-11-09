with open('text.txt') as file1, open('analysis.txt', 'w') as file2:
    alpha = {}
    count = 0
    for i in file1.readline().lower():
        if i.isalpha():
            count += 1
            if i not in alpha:
                alpha[i] = 1
            else:
                alpha[i] += 1
    for key, value in alpha.items():
        alpha[key] = round(value / count, 3)
    alpha = ([x, y] for x, y in sorted(alpha.items(), key=lambda x: (-x[1], x[0])))
    for k, c in alpha:
        file2.writelines(k + ' ' + str(c) + '\n')



