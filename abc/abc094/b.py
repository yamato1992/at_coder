n, m, x = map(int, input().split())
toll = [0] * n
a = list(map(int, input().split()))
for ai in a:
    toll[ai] = 1
ans = min(sum(toll[:x]), sum(toll[x:]))
print(ans)