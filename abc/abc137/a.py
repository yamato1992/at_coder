A, B = map(int, input().split())
plus = A + B
minus = A - B
multi = A * B
ans = plus if plus > minus else minus
ans = multi if multi > ans else ans
print(ans)