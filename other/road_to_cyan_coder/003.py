s = input()
words = 'ACGT'
ans = 0
cnt = 0
for c in s:
    if c in words:
        cnt += 1
    else:
        cnt = 0
    ans = max(ans, cnt)
print(ans)
