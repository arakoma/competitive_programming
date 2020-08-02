N, D = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for x, y in xy:
    if x ** 2 + y ** 2 <= D ** 2:
        ans += 1

print(ans)