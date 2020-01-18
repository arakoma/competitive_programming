H = int(input())
W = int(input())
N = int(input())

t = 0
ans = 0
for i in range(max(H, W)):
    t += max(H, W)
    ans += 1
    if t >= N:
        break

print(ans)