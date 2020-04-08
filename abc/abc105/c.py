n = int(input())

ans = []
while True:
    if n % 2 == 1:
        ans.append('1')
        n -= 1
    else:
        ans.append('0')
    n = n // (-2)
    if n == 0:
        break

print(''.join(ans[::-1]))
    