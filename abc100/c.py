N = int(input())

seq = list(map(int, input().split()))

cnt = 0

for num in seq:
    while num % 2 == 0:
        cnt += 1
        num /= 2

print(cnt)
