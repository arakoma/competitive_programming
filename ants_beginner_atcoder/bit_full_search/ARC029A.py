N = int(input())
t = [int(input()) for _ in range(N)]

ans = 9999999
for i in range(2 ** N):
    x = 0
    y = 0
    for j in range(N):
        if (i >> j) & 1:
            x += t[j]
        else:
            y += t[j]
    ans = min(ans, max(x, y))

print(ans)