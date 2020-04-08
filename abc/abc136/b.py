N = int(input())
cnt = 0
num = 1
while num <= N:
    cnt += 1
    num += 1
    if len(str(num)) % 2 == 0:
        num *= 10
print(cnt)