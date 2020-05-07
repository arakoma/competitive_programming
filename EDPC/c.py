N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(3):
        for k in range(3):
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abc[i-1][k])

print(max(dp[N]))