def dictionary(step):
    lst = []
    string = ''
    for i in step:
        lst += (step[i]['interests'])
        string += step[i]['surname']
    cnt = 0
    for _ in string:
        cnt += 1
    pairs = []
    num = []
    for x in students:
        num.append(x)
        pairs.append(students[x]['age'])
    out = list(zip(num, pairs))
    return lst, cnt, out

students = {

    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

my_lst = dictionary(students)[0]
items = dictionary(students)[1]
three = dictionary(students)[2]

print('Список пар "ID студента — возраст":', three)
print('Полный список интересов всех студентов:', set(my_lst))
print('Общая длина всех фамилий студентов:', items)



