N = int(input())
d = list(map(int, input().split()))
d.sort()
arc = d[N // 2]
abc = d[N // 2 - 1]
print(arc - abc)