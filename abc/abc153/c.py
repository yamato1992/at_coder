N, K = map(int, input().split())

hit_points = list(map(int, input().split()))
hit_points.sort()

for _ in range(K):
    if hit_points == []:
        break
    hit_points.pop()

print(sum(hit_points))
