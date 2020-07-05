N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0
if N >= 2:
    ans += A[0]

if N >= 3:
    idx = 1
    for i in range(N-2):
        ans += A[idx]
        if i % 2 == 1:
            idx += 1

print(ans)