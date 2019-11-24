N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

xy.sort(key=lambda x:(x[0],x[1]))
d1 = []
for i in range(1, N):
    x = xy[i-1][0] - xy[i][0]
    y = xy[i-1][1] - xy[i][1]
    d1.append((x, y))
P1 = 0
for D in d1:
    P1 = max(d1.count(D), P1)

xy.sort(key=lambda x:(x[0],x[1]), reverse=True)
d2 = []
for i in range(1, N):
    x = xy[i-1][0] - xy[i][0]
    y = xy[i-1][1] - xy[i][1]
    d2.append((x, y))
P2 = 0
for D in d2:
    P2 = max(d2.count(D), P2)


xy.sort(key=lambda x:(x[1],x[0]))
d3 = []
for i in range(1, N):
    x = xy[i-1][0] - xy[i][0]
    y = xy[i-1][1] - xy[i][1]
    d3.append((x, y))
P3 = 0
for D in d3:
    P3 = max(d3.count(D), P3)

xy.sort(key=lambda x:(x[1],x[0]), reverse=True)
d4 = []
for i in range(1, N):
    x = xy[i-1][0] - xy[i][0]
    y = xy[i-1][1] - xy[i][1]
    d4.append((x, y))
P4 = 0
for D in d4:
    P4 = max(d4.count(D), P4)

cut_P = max(P1,P2,P3,P4)
ans = N - cut_P
print(ans)


#x(or y)要素で同じのが続いた場合、それらの順番を変えた場合が考慮できてないかも


#################################
n = int(input())
balls = [set(map(int, input().split())) for _ in range(N)]

balls.sort()
ans = 0
for i in range(n - 1):
    x1, y1 = balls[i]
    for j in range(i + 1, n):
        x2, y2 = balls[j]
        p, q = x2 - x1, y2 - y1
        tmp = 0
        for x, y in balls:
            if (x - p, y - q) in balls:
                tmp += 1
        ans = max(ans, tmp)
print(n - ans)