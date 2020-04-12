n = int(input())
ans = 10 ** 9
for a in list(map(int, input().split())):
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    ans = min(ans, cnt) 
print(ans)
