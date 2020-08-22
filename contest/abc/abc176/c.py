N = int(input())
A = list(map(int, input().split()))

ans = 0
a_max = A[0]
for i in range(1, N):
    if A[i] < a_max:
        ans += a_max - A[i]
    else:
        a_max = A[i]

print(ans)
