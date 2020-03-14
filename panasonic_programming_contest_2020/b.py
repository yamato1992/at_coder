H, W = map(int, input().split())
if H >= 2 and W >= 2:
    ans = ((H + 1) // 2) * ((W + 1) // 2) + (H // 2) * (W // 2)
else:
    ans = 1
print(ans)