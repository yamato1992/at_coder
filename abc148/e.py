import math

N = int(input())

def double_factorial(num):
    if num < 10:
        return 1
    else:
        return num * double_factorial(num - 10)


res = double_factorial(N - (M % 10))
s = list(str(res))
ans = 0

for c in reversed(s):
    if c == '0':
        ans += 1
    else:
        break
print(ans)

# arr = [0] * 18

# ans = 0
# arr[1] = 12
# k = int(math.log10(N))
# for i in range(2, k):
#     arr[i]  = i + 9 * arr[i - 1] + 1 * i

print(arr)