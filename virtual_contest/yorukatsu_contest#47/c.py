n, m = map(int, input().split())
spots = list(map(int, input().split()))
spots.sort()
diff = []
for i in range(1, m):
    diff.append(abs(spots[i] - spots[i - 1]))
diff.sort(reverse=True)
ans = sum(diff[n - 1:])
print(ans)
