A, B = map(int, input().split())
space = A - B * 2
if space < 0:
    space = 0
print(space)