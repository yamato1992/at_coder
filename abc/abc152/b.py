a, b = input().split()

res_a = a * int(b)
res_b = b * int(a)

if res_a > res_b:
    print(res_b)
else:
    print(res_a)
