n = int(input())
s = input()
ans = 0
for i in range(10):
    for  j in range(10):
        for k in range(10):
            i_index = s.find(str(i))
            if i_index > - 1:
                j_index = s.find(str(j), i_index + 1)
                if j_index > -1:
                    k_index = s.find(str(k), j_index + 1)
                    if k_index > -1:
                        ans += 1
print(ans)