s = input()
n = len(s)

if n % 2 == 1:
    n -= 1

for i in range(n - 2, 0, -2):
    if s[:i//2] == s[i//2:i]:
        print(i)
        break
