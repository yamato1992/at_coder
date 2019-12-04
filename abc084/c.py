N = int(input())
params = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    time = 0
    for j in range(i, N - 1):
        c = params[j][0]
        s = params[j][1]
        f = params[j][2]
        if s > time:
            time += s - time + c
        else:
            time += (s - time) % f + c
    print(time)
    
print(0)
