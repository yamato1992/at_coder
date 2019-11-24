A, B, X = map(int, input().split())

low = 0
high = pow(10, 9) + 1

if A * pow(10, 9) + B * 10 < X:
    print(pow(10, 9))
    exit()

while high - low > 1:
    mid = (high + low) // 2

    if (A * mid + B * len(str(mid))) > X:
        high = mid
    else:
        low = mid

print(low)
