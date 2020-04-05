s = [int(c) for c in list(input())]
num = 753
ans = num
for i in range(len(s) - 2):
    x = s[i] * 10 ** 2 + s[i + 1] * 10 + s[i + 2]
    ans = min(ans, abs(num - x))
print(ans)