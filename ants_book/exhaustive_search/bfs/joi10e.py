from collections import deque

H, W, N = map(int, input().split())
maze = [list(input()) for _ in range(H)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(sy, sx, next_point):
    INF = 10**5
    d = [[10**5] * W for _ in range(H)]
    d[sy][sx] = 0
    q = deque()
    q.append((sy, sx))

    while len(q):
        y, x = q.popleft()

        if maze[y][x] == str(next_point):
            break

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < H and 0 <= nx < W and
                maze[ny][nx] != 'X' and d[ny][nx] == INF):

                q.append((ny, nx))
                d[ny][nx] = d[y][x] + 1

    return y, x, d[y][x]


ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            for k in range(1, N+1):
                i, j, time = bfs(i, j, k)
                ans += time
            break

print(ans)