from collections import defaultdict

n, m = map(int ,input().split())
drinks = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    drinks[a] += b

ans = 0
sorted_drinks = sorted(drinks.items(), key=lambda x:x[0])

for a, b in sorted_drinks:
    cnt = min(m, b)
    ans += a * cnt
    m -= cnt
    if m == 0:
        break
print(ans)    
