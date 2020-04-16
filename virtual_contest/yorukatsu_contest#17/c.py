n = int(input())
a = list(map(int, input().split()))
y1 = sum(a) // n
y2 = y1 + 1
y3 = y1 - 1

ans = 200 ** 2 * 100
tmp1 = 0
tmp2 = 0
tmp3 = 0
for x in a:
    tmp1 += (x - y1) ** 2
    tmp2 += (x - y2) ** 2
    tmp3 += (x - y3) ** 2
ans = min(ans, tmp1, tmp2, tmp3)

print(ans)