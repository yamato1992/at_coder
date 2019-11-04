s = input()
ans = []
for c in s:
    if c == 'B' and ans:
        ans.pop()
    elif c == '0' or c == '1':
        ans.append(c)
print(''.join(ans))