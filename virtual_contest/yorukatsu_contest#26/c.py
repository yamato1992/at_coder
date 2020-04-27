s = list(input())
t = list(input())
s.sort()
t.sort(reverse=True)
ans = 'Yes'
n = min(len(s), len(t))
if s[:n] == t[:n]:
    if len(s) >= len(t):
        ans = 'No'
else:
    for sc, tc in zip(s, t):
        if sc == tc:
            continue
        if sc > tc:
            ans = 'No'
        else:
            ans = 'Yes'
        break
print(ans)