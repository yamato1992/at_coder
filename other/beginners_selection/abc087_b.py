def coins():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    res = 0

    for i in range(0, a + 1):
        for j in range(0, b + 1):
            for k in range(0, c + 1):
                sum = (i * 500) + (j * 100) + (k * 50)
                if sum == x:
                    res += 1
    return res

print(coins())
