n, k = map(int, input().split())
p = list(map(int, input().split()))
e = []
for pi in p:
    e.append((pi + 1) / 2)

total = sum(e[:k])
ans = total
for i in range(0, n - k):
    total = total - e[i] + e[i + k]
    ans = max(ans, total)

print(ans)