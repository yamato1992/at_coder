N, Y = map(int, input().split())

upper_10thousand = Y // 10000
for i in range(upper_10thousand, -1, -1):
    upper_5thousand = (Y - 10000 * i) // 5000
    for j in range(upper_5thousand, -1, -1):
        k = (Y - 10000 * i - 5000 * j) // 1000
        if N == (i + j + k):
            print(i, j, k)
            exit()

print(-1, -1, -1)
