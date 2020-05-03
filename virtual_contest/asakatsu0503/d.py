n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

ai = numbers[-1]
r = ai / 2

for i in range(n - 1):
    if numbers[i] == r:
        ans = [ai, int(r)]
        break
    if numbers[i] > r:
        if numbers[i] - r < r - numbers[i - 1]:
            ans = [ai, numbers[i]]
        break
    ans = [ai, numbers[i]]

print(*ans)
