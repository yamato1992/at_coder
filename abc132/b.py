N = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(1, N - 1):
    if p[i] > p[i -1] and p[i] < p[i + 1]:
        cnt += 1
    elif p[i] < p[i - 1] and p[i] > p[i + 1]:
        cnt += 1

print(cnt)
