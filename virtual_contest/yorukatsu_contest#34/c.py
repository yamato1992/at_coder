n = int(input())
works = [list(map(int, input().split())) for _ in range(n)]
ans = 'Yes'
works.sort(key=lambda x: x[1])
time = 0
for a, b in works:
    time += a
    if time > b:
        ans = 'No'
        break
print(ans)