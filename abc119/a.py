import datetime

y, m, d = list(map(int, input().split('/')))
date = datetime.date(y, m, d) 
threthold = datetime.date(2019, 4, 30)
if date <= threthold:
    print('Heisei')
else:
    print('TBD')