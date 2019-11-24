W, H, N = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(N)]

x1 = 0 #左端
x2 = W #右端
y3 = 0 #下端
y4 = H #上端

# 白い4角形が最小になる上下左右を見つける
for x,y,a in xya:
    if a == 1:
        x1 = max(x1, x)
    elif a == 2:
        x2 = min(x2, x)
    elif a == 3:
        y3 = max(y3, y)
    elif a == 4:
        y4 = min(y4, y)
else:
    # 右端が左端より左, 上端が下端より下,だと全部黒
    if x2 <= x1 or y4 <= y3:
        print(0)
    else:
        print((x2-x1) * (y4-y3))