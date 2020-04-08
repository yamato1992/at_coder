S = list(input())
s = list(reversed(S))
ans = 0
for i in range(len(S)):
    if not S[i] == s[i]:
        ans += 1
print(ans // 2)
