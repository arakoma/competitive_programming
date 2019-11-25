N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

hh = sorted(h)
ans = 10 ** 9
for i in range(N-K+1):
    ans = min(ans, hh[i+K-1] - hh[i])

print(ans)