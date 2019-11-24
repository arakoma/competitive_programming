n, m, c = map(int, input().split())
b = list(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    x = 0 + c
    for j in range(m):
        x += b[j] * a[i][j]
    if x > 0:
        cnt += 1

print(cnt)
