x = int(input())
ans = 0
n = 100
while n < x:
    n = int(n * 1.01) 
    ans += 1
print(ans)