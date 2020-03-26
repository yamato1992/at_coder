N, M = map(int, input().split())
foods_likes = [0] * M
for _ in range(N):
    survey_result = list(map(int, input().split()))
    k = survey_result[0]
    a = survey_result[1:]
    for i in range(k):
        foods_likes[a[i] - 1] += 1
ans = 0
for likes in foods_likes:
    if likes == N:
        ans += 1
print(ans)
