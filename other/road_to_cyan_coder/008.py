n = int(input())
goods = [list(map(int, input().split())) for _ in range(n)]
position = set()

for a, b in goods:
    position.add(a)
    position.add(b)

position = list(position)
position.sort()

ans = 30 * 2 * 10 ** 9
for i in range(len(position)):
    for j in range(i, len(position)):
        l = position[i]
        r = position[j]
        total = 0
        for a, b in goods:
            if l <= a and b <= r:
                time = r - l
            elif l <= a and r < b:
                time = (b - l) + (b - r)
            elif a < l and l <= b <= r:
                time = (r - a) + (l - a)
            elif a < l and r < b:
                time = (b - a) + (l - a) + (b - r)
            elif a < l and b < l:
                time = (l - a) + (r - a)
            elif l <= a and r <= a:
                time = b - l
            total += time
        ans = min(ans, total)
print(ans)