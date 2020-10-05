N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

A = [a for a, b in AB]
B = [b for a, b in AB]

A.sort()
B.sort()

if N % 2 == 1:
    A_med = A[N//2]
    B_med = B[N//2]
else:
    A_med = (A[N//2-1] + A[N//2]) // 2
    B_med = (B[N//2-1] + B[N//2]) // 2

ans = 0
for a, b in AB:
    ans += abs(a - A_med) + (b - a) + abs(b - B_med)

print(ans)