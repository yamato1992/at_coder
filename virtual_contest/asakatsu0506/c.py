s = input()
multi_list = list(s.split('+'))
ans = 0
for f in multi_list:
    if '0' in f:
        continue
    ans += 1
print(ans)