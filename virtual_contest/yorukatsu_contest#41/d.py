n, k = map(int, input().split())
d = list(map(int, input().split()))
num = n
while True:
    is_match = True
    for c in str(num):
        if int(c) in d:
            is_match = False
            break
    if is_match:
        break
    num += 1
print(num)