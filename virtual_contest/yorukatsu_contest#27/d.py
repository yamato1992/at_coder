n = int(input())
A = list(map(int, input().split()))
num_minus = 0
minimum = 10 ** 6
ans = 0

for a in A:
    if a < 0:
        num_minus += 1
    minimum = min(minimum, abs(a))
    ans += abs(a)

if num_minus % 2 == 0:
    print(ans)
else:
    print(ans - minimum * 2)
