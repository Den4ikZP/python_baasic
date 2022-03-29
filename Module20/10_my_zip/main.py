def shortes(string, tpl):
    return min(len(string), len(tpl))

strip = 'abcd'
number = (10, 20, 30, 40)

pairs = ((strip[i_elem], number[i_elem])
         for i_elem in range(shortes(strip, number)))
print(pairs)

for i_elem in pairs:
    print(i_elem)


