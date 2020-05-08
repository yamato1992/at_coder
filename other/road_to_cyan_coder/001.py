n, x = map(int, input().split())
while n != 0 or x != 0:
    ans = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                if i + j + k == x:
                    ans += 1
    print(ans)
    n, x = map(int, input().split())