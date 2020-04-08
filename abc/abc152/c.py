N = int(input())
P = list(map(int, input().split()))

cnt = 1
min = P[0]

for i in range(1, len(P)):
    if P[i] < min:
        cnt += 1
        min = P[i]

print(cnt)