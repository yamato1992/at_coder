n = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0
a.sort(reverse=True)
for i, v in enumerate(a):
    if i % 2 == 0:
        alice += v
    else:
        bob += v
print(alice - bob)
