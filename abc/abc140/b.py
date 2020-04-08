N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
least = -1
for ai in a:
    ans += b[ai - 1]
    if ai - 1 == least:
        ans += c[least - 1]
    least = ai
print(ans)