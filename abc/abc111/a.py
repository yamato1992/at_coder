n = input()
ans = []
for c in n:
    if c == '1':
        ans.append('9')
    else:
        ans.append('1')
print(''.join(ans))