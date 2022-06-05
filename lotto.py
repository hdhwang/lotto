import random

alphabet_list = ['A', 'B', 'C', 'D', 'E']

for i in range(5):
    num_list = []
    ran_num = random.randint(1, 45)
    for j in range(6):
        while ran_num in num_list:
            ran_num = random.randint(1, 45)
        num_list.append(ran_num)

    num_list.sort()
    str_num_list = ''

    for k in range(6):
        str_num = '%02d' % num_list[k]
        str_num_list += str_num if str_num_list == '' else f' {str_num}'

    # print(f'{alphabet_list[i]} : {str_num_list}')
