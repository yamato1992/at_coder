h, w = map(int, input().split())
print('#' * (w + 2))
for _ in range(h):
    a = input()
    print('#' + a + '#')
print('#' * (w + 2))