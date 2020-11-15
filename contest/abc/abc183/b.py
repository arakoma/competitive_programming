sx, sy, gx, gy = map(int, input().split())
gy = - gy
ans = sx - sy * (gx - sx) / (gy - sy)
print(ans)