import random
from bs4 import BeautifulSoup
import requests

base_url = 'https://dhlottery.co.kr/gameResult.do?method=statByNumber'
con = requests.get(base_url)
soup = BeautifulSoup(con.content, 'html.parser')
stats_table = soup.find('table', {'class': 'tbl_data tbl_data_col'})

stats_list = []
ball_list = []

for tr in stats_table.find_all('tr'):
    ball_data = []
    for td in tr.find_all('td'):
        data = td.get_text()
        if '\n\n' not in data:
            ball_data.append(int(data))

    if ball_data:
        stats_list.append(ball_data)

for stats in stats_list:
    number = stats[0]
    count = stats[1]

    for i in range(count):
        ball_list.append(number)

random.shuffle(ball_list)

for i in range(5):
    num_list = []
    str_num_list = ''

    for j in range(6):
        lotto = random.choice(ball_list)
        while lotto in num_list:
            lotto = random.choice(ball_list)
        num_list.append(lotto)

    num_list.sort()

    for j in range(6):
        str_num = '%02d' % int(num_list[j])
        str_num_list += str_num if str_num_list == '' else f' {str_num}'

    print(f'{chr(i+65)} : {str_num_list}')
