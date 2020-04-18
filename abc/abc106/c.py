s = list(map(int, list(str(input()))))
k = int(input())

i = 0
while i + 1 <= k:
    ans = s[i]
    if s[i] != 1:
        break
    i += 1
print(ans)