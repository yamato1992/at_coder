a, b, c = map(int, input().split())
cnt = 0
total = a + b + c
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    if a == (total - a) // 2:
        cnt = -1
        break
    a = (total - a) // 2
    b = (total - b) // 2
    c = (total - c) // 2
    cnt += 1
print(cnt)