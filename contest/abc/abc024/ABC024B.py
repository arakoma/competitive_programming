N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

ans = 0
for i in range(N-1):
    if A[i] + T <= A[i+1]:
        ans += T
    else:
        ans += A[i+1] - A[i]
else:
    ans += T #最後

print(ans)