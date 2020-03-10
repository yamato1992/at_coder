N = int(input())
A = list(map(int, input().split()))

denominator = 0

for ai in A:
    denominator += 1 / ai

print(1 / denominator)