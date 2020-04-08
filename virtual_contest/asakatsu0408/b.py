n = int(input())
a = list(map(int, input().split()))
ans = 0
for num in a:
    ans += format(num, 'b')[::-1].find('1')
print(ans)