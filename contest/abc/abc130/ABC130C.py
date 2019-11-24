W, H, x, y = map(float, input().split())

D = W * H / 2
if x == W/2 and y == H/2:
    print(D, 1)
else:
    print(D, 0)