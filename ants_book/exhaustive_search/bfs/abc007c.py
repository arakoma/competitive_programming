from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
maze = [list(input()) for _ in range(R)]
sy -= 1
sx -= 1
gy -= 1
gx -= 1

INF = 10**5
d = [[10**5] * C for _ in range(R)]
q = deque()

d[sy][sx] = 0
q.append((sy, sx))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

#bfs
while len(q):
    y, x = q.popleft()

    if y == gy and x == gx:
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= ny < R and 0 <= nx < C and
            d[ny][nx] == INF and maze[ny][nx] != '#'):

            q.append((ny, nx))
            d[ny][nx] = d[y][x] + 1


print(d[gy][gx])