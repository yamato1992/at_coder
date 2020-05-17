x = int(input())
ans = 1
for i in range(2, x + 1):
    j = 2
    while i ** j <= x:
        ans = max(ans, i ** j)
        j += 1
print(ans)
