H, W = map(int, input().split())

ans = 0
if H == 1 or W == 1:
    ans = 1
elif H % 2 == 0:
    ans = (W * H) // 2
else:
    ans = (W * (H - 1)) // 2 + (W + 1) // 2

print(ans)