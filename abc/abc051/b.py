k, s = map(int, input().split())
pattern = 0

for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if z <= k and z >= 0:
            pattern += 1

print(pattern)
