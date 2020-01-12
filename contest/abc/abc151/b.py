N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if 0 >= M * N - sum(A):
    print(0)
elif K >= M * N - sum(A) > 0:
    print(M * N - sum(A))
else:
    print(-1)