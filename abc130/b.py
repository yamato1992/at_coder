N, X = map(int, input().split())
L = list(map(int, input().split()))
cnt = 1
di = 0

for li in L:
    di += li
    if di > X:
        break
    cnt += 1

print(cnt)