N, K = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(K):
    B = [0] * N
    for i, d in enumerate(A):
        l = max(0, i-d)
        r = min(N-1, i+d)
        B[l] += 1
        if r+1 < N:
            B[r+1] -= 1
    
    for i in range(1, N):
        B[i] += B[i-1]
    
    A = B.copy()
    if min(A) == N:
        break

print(" ".join(map(str, A)))