def tpl_sort():
    a = (6, 3, -1, 8, 4, 10, -5)
    flag = True
    for i in a:
        if i != int(i):
            flag = False
    if flag:
        return tuple(sorted(a))
    return a
print(tpl_sort())


