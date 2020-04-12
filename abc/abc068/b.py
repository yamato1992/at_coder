n = int(input())
ans = 1

while True:
    if ans * 2 > n:
        break
    ans *= 2
print(ans)
