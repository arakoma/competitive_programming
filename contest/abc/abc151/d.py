from collections import deque


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

INF = 10 ** 6
visited = [[10 ** 6] * W for _ in range(H)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(y, x):
    q = deque()
    q.append((y, x))

    while len(q):
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < H and 0 <= nx < W and
                visited[ny][nx] == INF and S[ny][nx] != '#'):

                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] != "#":
            visited = [[10 ** 6] * W for _ in range(H)]
            visited[y][x] = 0
            bfs(y, x)
            for i in range(H):
                for j in range(W):
                    if visited[i][j] != INF:
                        ans = max(ans, visited[i][j])

print(ans)