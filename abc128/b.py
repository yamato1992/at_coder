N = int(input())
city = dict()
restaurants = []
for _ in range(N):
    s, p = input().split()
    restaurants.append([s, int(p)])
    if s in city.keys():
        city[s].append(int(p))
    else:
        city[s] = [int(p)]

city = sorted(city.items(), key=lambda x:x[0])

for c in city:
    points = c[1]
    points.sort(reverse=True)
    for p in points:
        for i in range(N):
            s = c[0]
            r = restaurants[i]
            if r[0] == s and r[1] == p:
                print(i + 1)