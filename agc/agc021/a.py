n = list(map(int, list(str(input()))))
ans = sum(n)
ans = max(ans, n[0] - 1 + 9 * (len(n) - 1))
print(ans)