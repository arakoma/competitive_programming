N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

sum_before = sum(T)
for i in range(M):
    sum_after = sum_before - T[PX[i][0]-1] + PX[i][1]
    print(sum_after)