N, D, H = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(N)]

a = 0
b = 0
ans = H

for d, h in dh:
    a = (H - h) / (D - d)
    b = h - a * d
    if b < 0:
        a = H / D
        b = 0
    for x, y in dh:
        if a * x + b < y:
            break
    else:
        ans = min(ans, b)

print(ans)
