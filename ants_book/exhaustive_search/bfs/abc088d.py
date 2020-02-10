from collections import deque

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

INF = 10**5
d = [[10**5] * W for _ in range(H)]
d[0][0] = 0

q = deque()
q.append((0, 0))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while len(q):
    y, x = q.popleft()

    if y == H-1 and x == W-1:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < H and 0 <= nx < W and
            maze[ny][nx] != '#' and d[ny][nx] == INF):

            d[ny][nx] = d[y][x] + 1
            q.append((ny, nx))

if d[H-1][W-1] == INF:
    print(-1)
else:
    black = 0
    for a in maze:
        black += a.count('#')
    
    print(H * W - black - d[H-1][W-1] - 1)