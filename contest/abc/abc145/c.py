N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]


def xxx(n):
    if n == 0:
        return 1
    else:
        return n * xxx(n-1)


d = 0
for i in range(N-1):
    for j in range(i+1, N):
        d += xxx(N - 1) * 2 * ((xy[i][0] - xy[j][0])**2 + (xy[i][1] - xy[j][1])**2) ** 0.5

ans = d / xxx(N)
print(ans)