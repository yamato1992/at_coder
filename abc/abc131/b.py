N, L = map(int, input().split())
diff_min = 100 + 200 - 1
apples = list()
remove_apple = 0

for i in range(N):
    taste = L + i
    apples.append(taste)
    if abs(taste) < diff_min:
        diff_min = abs(taste)
        remove_apple = taste

print(sum(apples) - remove_apple)
