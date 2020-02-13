N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ab.sort(key=lambda x: x[1])
ans = 0
x = -9999999999
for a, b in ab:
    if x <= a:
        x = b
        ans += 1

print(ans)