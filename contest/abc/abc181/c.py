N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

ans = "No"
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            x3, y3 = xy[k]
            if (x1 - x2) * (y2 - y3) == (x2 - x3) * (y1 - y2):
                ans = "Yes"

print(ans)