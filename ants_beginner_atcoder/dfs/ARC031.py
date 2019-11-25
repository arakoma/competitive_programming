# 2(以上)次元配列のコピーはdeepcopy使う
# (copyやスライスだと、配列内の配列が参照渡しのままになる)
from copy import deepcopy
import sys


def dfs(y, x):
    #範囲外ならスルー
    if not(0 <= y < 10 and 0 <= x < 10):
        return
    #海ならスルー
    elif m[y][x] == 'x':
        return
    #陸なら海にする
    elif m[y][x] == 'o':
        m[y][x] = 'x'
    
    #上下左右を探索
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)


sys.setrecursionlimit(10 ** 6)

M = [list(input()) for _ in range(10)]

for i in range(10):
    for j in range(10):
        cnt = 0
        m = deepcopy(M)
        m[i][j] = 'o'
        for k in range(10):
            for l in range(10):
                if m[k][l] == 'o':
                    dfs(k, l)
                    cnt += 1
        if cnt == 1:
            print("YES")
            sys.exit()
else:
    print("NO")