from collections import defaultdict
S = input()
T = input()
s_map = defaultdict(str)
t_map = defaultdict(str)
ans = 'Yes'
for s, t in zip(S, T):
    if len(s_map[s]) > 0:
        if s_map[s] != t:
            ans = 'No'
    if len(t_map[t]) > 0:
        if t_map[t] != s:
            ans = 'No'
    s_map[s] = t
    t_map[t] = s

print(ans)