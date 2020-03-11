N = int(input())
cnt_dict = dict()

for _ in range(N):
    s = ''.join(sorted(list(input())))
    if s in cnt_dict:
        cnt_dict[s] += 1
    else:
        cnt_dict[s] = 1

ans = 0
for cnt in cnt_dict.values():
    ans += cnt * (cnt - 1) / 2

print(ans)
    