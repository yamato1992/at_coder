x = int(input())
for i in range(1, x + 1):
    p = ((i + 1) * i) // 2
    if p >= x:
        ans = i
        break
print(ans)