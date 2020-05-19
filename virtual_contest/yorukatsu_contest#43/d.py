n = int(input())
testimony = []

for _ in range(n):
    a = int(input())
    tmp = []
    for _ in range(a):
        x, y = map(int, input().split())
        x -= 1
        tmp.append((x, y))
    testimony.append(tmp)

ans = 0
for p in range(2 ** n):
    cnt = 0
    is_unmatch = False
    for i in range(n):
        if p >> i & 1:
            cnt += 1
            for x, y in testimony[i]:
                if p >> x & 1 != y:
                    is_unmatch = True
                    break
        if is_unmatch:
            cnt = 0
            break
    ans = max(ans, cnt)

print(ans)