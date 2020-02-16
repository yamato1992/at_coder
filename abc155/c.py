N = int(input())
d = dict()
m = 0
for _ in range(N):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
    if d[s] > m:
        m = d[s]

sd = sorted(d.items(), reverse=True, key=lambda x:x[1])
ans = []
for k, v in sd:
    if v == m:
        ans.append(k)
    else:
        break

for a in sorted(ans):
    print(a)