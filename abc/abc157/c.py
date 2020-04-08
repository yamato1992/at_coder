import math

N, M = map(int, input().split())

candidate = []
for i in range(1000):
    if N == len(str(i)):
        candidate.append(i)

for _ in range(M):
    s, c = map(int, input().split())
    tmp = []
    for n in candidate:
        if int(str(n)[s - 1]) == c:
            tmp.append(n)
    candidate = tmp

if candidate:
    print(candidate[0])
else:
    print(-1)