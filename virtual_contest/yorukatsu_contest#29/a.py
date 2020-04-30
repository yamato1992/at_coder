n, x = map(int, input().split())
L = list(map(int, input().split()))

point = 0
ans = 1

for l in L:
    point += l
    if point > x:
        break
    ans += 1

print(ans)
