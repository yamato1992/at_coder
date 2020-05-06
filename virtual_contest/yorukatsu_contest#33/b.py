n = int(input())
buttons = [int(input()) for _ in range(n)]
pushed = [False] * n
b = 0
ans = 0
while True:
    ans += 1
    pushed[b] = True
    b = buttons[b] - 1
    if pushed[b]:
        ans = -1
        break
    if b == 1:
        break
        
print(ans)
