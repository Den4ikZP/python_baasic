########## Вариант 1 ##########

import random

one = []
two = []
[one.append(random.randint(1, 101)) for i in range(5)]
[two.append(random.randint(1, 101)) for x in range(5)]

print(list(zip(one, two)))


########## Вариант 2 ##########



one_1 = []
two_2 = []
three = []

[one_1.append(random.randint(1, 101)) for o in range(10)]
[two_2.append(x[1]) if x[0] % 2 == 0 else three.append(x[1]) for x in enumerate(one_1)]

print(list(zip(two_2, three)))