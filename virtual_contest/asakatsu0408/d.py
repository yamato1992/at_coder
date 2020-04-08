s = input()

while len(s) > 4:
    if s[-5:] == 'dream':
        s = s[:-5]
    elif s[-7:] == 'dreamer':
        s = s[:-7]
    elif s[-5:] == 'erase':
        s = s[:-5]
    elif s[-6:] == 'eraser':
        s = s[:-6]
    else:
        break

print('NO' if len(s) > 0 else 'YES')
