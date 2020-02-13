N = int(input())
XL = [list(map(int, input().split())) for _ in range(N)]

XL.sort(key=lambda x: sum(x))
f = -99999999999
ans = 0
for x, l in XL:
    if x - l >= f:
        ans += 1
        f = x + l

print(ans)