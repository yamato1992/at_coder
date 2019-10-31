s = input()
remain = s.replace('eraser', '').replace('erase', '').replace('dreamer', '').replace('dream', '')
if remain == '':
    print('YES')
else:
    print('NO')
    