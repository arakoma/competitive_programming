n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
xy_set = set(xy)

ans = 0

for i in range(n):
    for j in range(i+1, n):
        x1, y1 = xy[i]
        x2, y2 = xy[j]

        # xy3, xy4 の座標を求めてあるかどうか探索
        x3 = x2 + (y2 - y1) 
        y3 = y2 - (x2 - x1)
        x4 = x1 + (y2 - y1)
        y4 = y1 - (x2 - x1)

        if (x3, y3) in xy_set and (x4, y4) in xy_set:
            s = (x1 - x2) ** 2 + (y1 - y2) ** 2
            ans = max(ans, s)

print(ans)