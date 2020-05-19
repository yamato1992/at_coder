a, b = map(int, input().split())
ans = -1
for x in range(13, 1250):
    if int(x * 0.08) == a and int(x * 0.1) == b:
        ans = x
        break
print(ans)