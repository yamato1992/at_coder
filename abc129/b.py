N = int(input())
W = list(map(int, input().split()))
s1 = W[0]
s2 = sum(W[1:])
diff = abs(s1 - s2)

for i in range(1, N):
    s1 += W[i]
    s2 -= W[i]
    diff = min(diff, abs(s1 - s2))

print(diff)
