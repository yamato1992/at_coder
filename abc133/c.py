L, R = map(int, input().split())
end = min(R, L + 4038)
ans = 2018

for a in range(L, end):
    for b in range(a + 1, end+ 1):
        tmp = (a * b) % 2019
        if tmp < ans:
            ans = tmp

print(ans)
