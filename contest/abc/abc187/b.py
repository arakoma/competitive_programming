N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    for j in range(i, N):
        xi, yi = xy[i]
        xj, yj = xy[j]
        if xi - xj == 0:
            continue
        if -1 <= (yi - yj) / (xi - xj) <= 1:
            ans += 1

print(ans)