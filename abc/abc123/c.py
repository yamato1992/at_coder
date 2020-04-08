import math

N = int(input())
T = [int(input()) for _ in range(5)]

t_min = min(T)
bottle = math.ceil(N / t_min)
print(5 + (bottle - 1))