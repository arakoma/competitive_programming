H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

min_a = 999999
for a in A:
    min_a = min(min_a, min(a))

ans = 0
for h in range(H):
    for w in range(W):
        ans += max(0, A[h][w] - min_a)

print(ans)