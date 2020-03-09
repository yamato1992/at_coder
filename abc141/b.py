S = list(input())
ans = 'Yes'
for i in range(len(S)):
    if (i + 1) % 2 == 0 and S[i] == 'R':
        ans = 'No'
    if (i + 1) % 2 == 1 and S[i] == 'L':
        ans = 'No'
print(ans)