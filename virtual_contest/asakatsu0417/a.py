n, l = map(int, input().split())
diff = 300
ans = [0] * n
p = 0
for i in range(n):
    taste = l + i
    ans[i] = taste
    if diff > abs(taste):
        diff = abs(taste)
        p = i
print(sum(ans) - ans[p])