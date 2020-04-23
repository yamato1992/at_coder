x = int(input())
ans = 1
for i in range(2, int(x ** 0.5) + 1):
    j = 1
    while i ** j <= x:
        ans = max(ans, i ** j)
        j += 1
print(ans)
