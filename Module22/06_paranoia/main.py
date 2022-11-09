def cesar_chipser(num, word):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([alpha[(alpha.index(i) + num) % 52] for i in word])



with open('cipher_text.txt', 'w') as f:
    for x, y in enumerate(open('text.txt'), 1):
        result = cesar_chipser(x, y.strip())
        f.write(result + '\n')

