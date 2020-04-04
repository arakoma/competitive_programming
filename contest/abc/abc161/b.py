N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
sum_A = sum(A)
for a in A:
    if a >= sum_A / (4 * M):
        cnt += 1

if cnt >= M:
    ans = "Yes"
else:
    ans = "No"

print(ans)