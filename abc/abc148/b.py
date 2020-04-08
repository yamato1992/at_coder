N = int(input())
S, T = map(list, input().split())
ans = ''
for a, b in zip(S, T):
    ans += a + b
print(ans)