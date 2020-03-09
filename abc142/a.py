N = int(input())
odds = N // 2
if N % 2 == 1:
    odds += 1
print(odds / N)