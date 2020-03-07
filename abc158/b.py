N, A, B = map(int, input().split())
ab = A + B
cnt = N // ab
remain = N - (cnt * ab)
blue = 0
if remain > A:
    blue = A
else:
    blue = remain
ans = A * cnt + blue
print(ans)