N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
s = sum(A)

ans = 0
for i in range(N):
    ans += A[i] * (N - i - 1) - (s - A[i])
    s -= A[i]

print(ans)