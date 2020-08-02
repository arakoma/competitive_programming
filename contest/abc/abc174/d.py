N = int(input())
C = list(input())

cnt = 0
C_sort = sorted(C)
for i in range(N):
    if C[i] != C_sort[i]:
        cnt += 1

print(cnt // 2)