N = int(input())
bricks = map(int, input().split())
 
ans = 0
num = 1
 
for a in bricks:
    if a == num:
        num += 1
    else:
        ans += 1
 
if ans == N:
    ans = -1
 
print(ans)