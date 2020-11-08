N = int(input())
A = list(map(int, input().split()))

ruiseki = [0 for _ in range(N+1)]
r_max = [0 for _ in range(N+1)]
for i in range(1, N+1):
    ruiseki[i] = ruiseki[i-1] + A[i-1]
for i in range(1, N+1):
    r_max[i] = max(r_max[i-1], ruiseki[i])

ans = 0
now = 0
for i in range(N):
    now += ruiseki[i] + A[i]
    if ans < now + r_max[i] and i != N-1:
        ans = now + r_max[i]
ans = max(ans, now)
print(ans)