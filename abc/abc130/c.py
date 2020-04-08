W, H, x, y = map(int, input().split())

ans = W * H / 2
n = 1 if W == x * 2 and H == y * 2 else 0
print(ans, n)
