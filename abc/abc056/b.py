w, a, b = map(int, input().split())
a_tail = a + w
b_tail = b + w

if (a >= b and a <= b_tail) or (a_tail >= b and a_tail <= b_tail):
    ans = 0
else:
    ans = min(abs(a + w -b), abs(b + w - a))

print(ans)