import sys
sys.setrecursionlimit(10**6)

X, Y = map(int, input().split())

def dfs(x, y):
    if x == X and y == Y:
        return 1
    if x > X or y > Y:
        return 0
    return dfs(x + 1, y + 2) + dfs(x + 2, y + 1)

print(dfs(0, 0) % (pow(10, 9) + 7))
