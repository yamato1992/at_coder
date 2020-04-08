S = list(input())
char_cnt = dict()
cnt = 2
ans = 'Yes'

for s in S:
    if s in char_cnt:
        char_cnt[s] += 1
    else:
        char_cnt[s] = 1

for n in char_cnt.values():
    if n != cnt:
        ans = 'No'

print(ans)
