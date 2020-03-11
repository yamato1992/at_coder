K, X = map(int, input().split())
start = (X - (K - 1))
end = (X + (K - 1))
upper = 1000000
lower = -1000000

if start < lower:
    start = lower

if end > upper:
    end = upper

print(' '.join([str(n) for n in range(start, end + 1)]))