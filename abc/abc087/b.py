a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
a_lim = min(a, x // 500) + 1
total = x
for i in range(a_lim):
    a_total = total - 500 * i
    b_lim = min(b, a_total // 100) + 1
    for j in range(b_lim):
        b_total = a_total - 100 * j
        if b_total // 50 <= c:
            ans += 1
print(ans)