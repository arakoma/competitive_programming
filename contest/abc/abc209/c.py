N = int(input())
C = list(map(int, input().split()))

C.sort()

ans = 1
mod = 10**9+7

for i in range(N):
    ans = (ans * (C[i] - i)) % mod

print(ans)