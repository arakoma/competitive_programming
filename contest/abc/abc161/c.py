N, K = map(int, input().split())

ans = 10 ** 18
if N == K:
    ans = 0
elif N < K:
    ans = min(N, abs(N - K))
elif N > K:
    ans = min(N % K, abs(N % K - K))

print(ans)