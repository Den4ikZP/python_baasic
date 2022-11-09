from zipfile import ZipFile
with ZipFile('voyna-i-mir.zip') as zFile:
    zFile.extractall()
with open('voyna-i-mir.txt', encoding='utf-8') as file1:
    alpha = {}
    count = 0
    for i in file1.readlines():
        i = i.strip()
        for j in i:
            if j.isalpha():
                count += 1
                if j not in alpha:
                    alpha[j] = 1
                else:
                    alpha[j] += 1
    for key, value in alpha.items():
        alpha[key] = round(value / count, 2)
    alpha = ([x, y] for x, y in sorted(alpha.items(), key=lambda x: x[1]))
    print(list(alpha))

