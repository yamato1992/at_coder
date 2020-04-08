n, a, b = map(int, input().split())
total = 0
for i in range(1, n + 1):
    wa = sum(list(map(int, list(str(i)))))
    if wa >= a and b >= wa:
        total += i
print(total)