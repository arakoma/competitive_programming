#####再帰で実装
#再帰の上限上げないとREする(上限のデフォルトは1000)
import sys
sys.setrecursionlimit(10 ** 6)

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

passed_flag = [[0]*W for _ in range(H)]


def dfs(y, x):
    #範囲外or壁orすでに通った
    if not (0 <= y < H and 0 <= x < W):
        return
    elif maze[y][x] == '#':
        return
    elif passed_flag[y][x]:
        return
    
    #通るならflag立てる
    passed_flag[y][x] = 1
    
    #左右上下を探索
    dfs(y, x - 1)
    dfs(y, x + 1)
    dfs(y - 1, x)
    dfs(y + 1, x)


for h in range(H):
    for w in range(W):
        if maze[h][w] == 's':
            sy = h
            sx = w
        elif maze[h][w] == 'g':
            gy = h
            gx = w

dfs(sy, sx)
if passed_flag[gy][gx]:
    print("Yes")
else:
    print("No")


#####stackで実装
from collections import deque
import sys

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if maze[i][j] == 's':
            sh = i
            sw = j

stack = deque([(sh, sw)])
visited = [[0] * W for _ in range(H)]
while stack:
    y, x = stack.pop()
    visited[y][x] = 1
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]: #上下左右
        dy = y + i
        dx = x + j
        if not (0 <= dy < H and 0 <= dx < W):
            continue
        elif maze[dy][dx] == '#':
            continue
        elif visited[dy][dx] == 1:
            continue
        elif maze[dy][dx] == 'g':
            print("Yes")
            sys.exit()
        else:
            stack.append((dy, dx))
else:
    print("No")