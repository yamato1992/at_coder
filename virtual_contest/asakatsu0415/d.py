lim = 10 ** 5
prime = [1] * (lim + 1) 
like = [0] * (lim + 1)
prime[0] = 0
prime[1] = 0

for i in range(2, lim + 1):
    if prime[i]:
        for j in range(i ** 2, lim + 1, i):
            prime[j] = 0

for i in range(3, lim + 1, 2):
    if prime[i] and prime[(i + 1) // 2]:
        like[i] = 1

for i in range(2, lim + 1):
    like[i] += like[i - 1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    x = like[r] - like[l - 1]
    print(x)