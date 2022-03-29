def checking_array(checking_list):
    return [v for i, v in enumerate(checking_list) if is_prime(i)]

def is_prime(i_num):
    for i in range(2, i_num):
        if i_num % i == 0:
            return False
    return True

s = input('Введите текст: ')

i_list = checking_array(s)
print(i_list[2:])
