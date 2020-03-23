from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
balls = defaultdict(int)
default_pattern = defaultdict(int)
pick_pattern = defaultdict(int)

for ai in A:
    balls[ai] += 1

total = 0
for k, v in balls.items():
    remain_balls = v - 1
    if v <= 1:
        default_pattern[k] = 0
    else:
        default_pattern[k] = (v * (v - 1)) // 2
        total += (v * (v - 1)) // 2

    if remain_balls <= 1:
        pick_pattern[k] = 0
    else:
        pick_pattern[k] = (remain_balls * (remain_balls - 1) // 2)

for ai in A:
    ans = total
    print(ans - default_pattern[ai] + pick_pattern[ai])