from collections import deque


H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

INF = 10 ** 5
d = [[10 ** 5] * W for _ in range(H)]

q = deque()

for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            d[i][j] = 0
            q.append((i, j))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

ans = 0
while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < H and 0 <= nx < W and
            A[ny][nx] != '#' and d[ny][nx] == INF):

            d[ny][nx] = d[y][x] + 1
            q.append((ny, nx))
            ans = max(ans, d[ny][nx])

print(ans)