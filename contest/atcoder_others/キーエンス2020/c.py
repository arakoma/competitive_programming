N, K, S = map(int, input().split())

A = [S] * K
if S != 10**9:
    A += [10**9] * (N - K)
else:
    A += [1] * (N - K)

print(" ".join(list(map(str, A))))