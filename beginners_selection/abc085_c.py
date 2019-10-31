def otoshidama(N, Y, a, b, c):
    cap_x = min(N, Y // a)
    for x in range(cap_x, -1, -1):
        cap_y = min(N - x, (Y - x * a) // b)
        for y in range(cap_y, -1, -1):
            z = N - x - y
            if (x * a + y * b + z * c) == Y:
                return [x, y, z]
    return [-1, -1, -1]

N, Y = map(int, input().split())
a, b, c = 10000, 5000, 1000

res = otoshidama(N, Y, a, b, c)
print(' '.join(list(map(str, res))))
