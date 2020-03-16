X, Y = map(int, input().split())
ans = 0
for _ in range(2):
    if X > Y:
        ans += X
        X -= 1
    else:
        ans += Y
        Y -= 1
print(ans)