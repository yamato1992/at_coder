s = list(map(int, list(str(input()))))
n = len(s)
ans = 0
for i in range(1 << n - 1):
    tmp = s[0]
    for j in range(n - 1):
        if (i >> j) & 1:
            ans += tmp
            tmp = s[j + 1]
        else:
            if j == 0:
                tmp = s[j] * 10 + s[j + 1]
            else:
                tmp = tmp * 10 + s[j + 1]
    ans += tmp
print(ans)
