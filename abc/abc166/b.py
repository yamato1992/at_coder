n, k = map(int, input().split())
snuke = set()

for _ in range(k):
    d = int(input())
    A = list(map(int, input().split()))
    snuke.update(set(A))

ans = n - len(snuke)
print(ans)