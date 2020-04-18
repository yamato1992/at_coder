x, y = map(int, input().split())

cnt = 0
tmp = x
while tmp <= y:
    tmp *= 2
    cnt += 1
print(cnt)
