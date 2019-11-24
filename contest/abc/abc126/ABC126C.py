N, K = map(int, input().split())

P = 0
for i in range(1, N+1):
    if i < K:
        cnt = 0
        while True:
            i *= 2
            cnt += 1
            if i >= K:
                P += 1 / (2 ** cnt)
                break
    else:
        P += 1

print(P / N)