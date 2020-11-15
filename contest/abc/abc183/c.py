N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def dfs(city, prev, next, t):
    if len(city) == 0:
        t += T[prev][next]
        t += T[next][0]
        if t == K:
            global ans
            ans += 1
            return
    t += T[prev][next]
    for c in city:
        city2 = city.copy()
        city2.remove(c)
        dfs(city2, next, c, t)

for i in range(1, N):
    dfs(list(range(1, N)), 0, i, 0)

print(ans)
