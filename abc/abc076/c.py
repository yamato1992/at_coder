import copy

S = list(input())
T = list(input())

ans = 'UNRESTORABLE'
len_s = len(S)
len_t = len(T)

is_matched = False

for i in range(len_s - len_t + 1):
    s = copy.deepcopy(S)
    for j in range(len_t):
        sc = s[(-1) - i - j]
        tc = T[(-1) - j]
        if sc == tc or sc == '?':
            s[(-1) - i - j] = tc
            if len_t == (j + 1):
                is_matched = True
        else:
            break
    if  is_matched:
        ans = ''.join(s).replace('?', 'a')
        break
print(ans)
