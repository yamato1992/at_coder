k, s = map(int, input().split())
diff = 3 * k - s
ans = 0
low = max(0, k - diff)
for x in range(low, k + 1):
    for y in range(low, k + 1):
        if k >= s - x - y and s - x - y >= 0:
            ans += 1
print(ans)