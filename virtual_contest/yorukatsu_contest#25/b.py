n = int(input())
kinds = set()
rainbow = 0
for a in list(map(int, input().split())):
    color = a // 400
    if color < 8:
        kinds.add(color)
    else:
        rainbow += 1

print(max(len(kinds), 1), len(kinds) + rainbow)
