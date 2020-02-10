from collections import deque


H, W = map(int, input().split())
c = [list(input()) for _ in range(H)]

INF = 10 ** 6
d = [[10 ** 6] * W for _ in range(H)]

q = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs_01():
    while q:
        y, x = q.popleft()

        if c[y][x] == 'g':
            return d[y][x]
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] == INF:
                if c[ny][nx] == '#':
                    q.append((ny, nx))
                    d[ny][nx] = d[y][x] + 1
                else:
                    q.appendleft((ny, nx))
                    d[ny][nx] = d[y][x]


for i in range(H):
    for j in range(W):
        if c[i][j] == 's':
            q.append((i, j))
            d[i][j] = 0

            if bfs_01() <= 2:
                print("YES")
            else:
                print("NO")