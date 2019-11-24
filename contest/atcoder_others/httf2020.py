#時間取得
import time

#再帰上限
import sys
sys.setrecursionlimit(10 ** 6)

"""
#input for txtfile
path = "example_01.txt"
with open(path) as f:
    N, M, B = map(int, f.readline().split())
    gy, gx = map(int, f.readline().split())
    robot = []
    for _ in range(M):
        ry, rx, c = f.readline().split()
        ry = int(ry)
        rx = int(rx)
        robot.append((ry, rx, c))
    brock = [tuple(map(int, f.readline().split())) for _ in range(B)]
"""

#input
N, M, B = map(int, input().split())
gy, gx = map(int, input().split())
robot = []
for _ in range(M):
    ry, rx, c = input().split()
    ry = int(ry)
    rx = int(rx)
    robot.append((ry, rx, c))
brock = [tuple(map(int, input().split())) for _ in range(B)]


#マス全体
square_map = [[0] * N for _ in range(N)]
square_map[gy][gx] = 'g'
for ry, rx, c in robot:
    square_map[ry][rx] = 'r'
for by, bx in brock:
    square_map[by][bx] = 'b'

#標識の座標と向き(output)を格納
sign = []

#上下左右
dydx = [(-1, 0), (1, 0), (0, -1), (0, 1)]
UDLR = ['U', 'D', 'L', 'R']

#上下左右の逆(下上右左)
UDLR_rev = ['D', 'U', 'R', 'L']


#output
def output():
    print(len(sign))
    for i in range(len(sign)):
        print(" ".join(sign[i]))


#output for txtfile
def output_txt():
    path_out = "01.txt"
    with open(path_out, mode='w') as f:
        f.write(str(len(sign)) + "\n")
        for i in range(len(sign)):
            f.write(" ".join(sign[i]) + "\n")


#一定時間経過したかを真偽で返す
def is_timelimit(start, limit):
    t = time.time() - start
    if t >= limit:
        start = time.time()#リセット
        return True
    else:
        return False


#隣接するマスの座標を返す
def next_yx(y, x, dy, dx):
    y_next = y + dy
    x_next = x + dx

    if y_next < 0:
        y_next = N - 1
    elif y_next > N - 1:
        y_next = 0
    
    if x_next < 0:
        x_next = N - 1
    elif x_next > N - 1:
        x_next = 0
    
    return y_next, x_next


#dfs
def dfs(y, x, direction):
    if square_map[y][x] == 'b':
        return
    elif square_map[y][x] == 's':
        return
    elif square_map[y][x] == 'g':
        return
    elif square_map[y][x] == 'x':
        return
    elif is_timelimit(start, 0.74):
        return

    sign.append((str(y), str(x), direction))
    square_map[y][x] = 's'

    for i in range(4):
        dy, dx = dydx[i]
        next_y, next_x = next_yx(y, x, dy, dx)
        dfs(next_y, next_x, UDLR_rev[i])


#壁に囲まれかけてるとこをつぶす
for i in range(N):
    for j in range(N):
        if square_map[i][j] == 0:
            cnt = 0
            for dy, dx in dydx:
                next_y, next_x = next_yx(i, j, dy, dx)
                if square_map[next_y][next_x] in ('b',):
                    cnt += 1
                if square_map[next_y][next_x] in ('g', 'r'):
                    break
            else:
                if cnt >= 3:
                    square_map[i][j] = 'x'

#ゴールマスからdfs
start = time.time()
for i in range(4):
    dy, dx = dydx[i]
    next_y, next_x = next_yx(gy, gx, dy, dx)
    dfs(next_y, next_x, UDLR_rev[i])


output()
#output_txt()