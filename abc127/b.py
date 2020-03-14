r, D, x = map(int, input().split())
last = x
for i in range(1, 11):
    last = r * last - D
    print(last)