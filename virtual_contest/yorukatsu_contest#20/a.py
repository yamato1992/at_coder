dishes = []
for i in range(5):
    time = int(input())
    diff = (10 - time % 10) % 10
    dishes.append([time, diff])
dishes = sorted(dishes, key=lambda x: x[1])
ans = 0
for i in range(4):
    time = dishes[i][0]
    ans += time + dishes[i][1]
ans += dishes[-1][0]
print(ans)