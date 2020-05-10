n, k = map(int, input().split())
teleporter = list(map(int, input().split()))
loop = [0]
checked = [False] * n
checked[0] = True
next_teleporter = teleporter[0] - 1

while not checked[next_teleporter]:
    checked[next_teleporter] = True
    loop.append(next_teleporter)
    next_teleporter = teleporter[next_teleporter] - 1

if next_teleporter == loop[0] - 1:
    index = k % len(loop)
    print(loop[index] + 1)
else:
    for i in range(len(loop)):
        if next_teleporter == loop[i]:
            s = i
            break
    if s > k:
        print(loop[k] + 1)
    else:
        loop = loop[s:]
        index = (k - s) % len(loop)
        print(loop[index] + 1)
