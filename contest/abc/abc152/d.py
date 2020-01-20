N = int(input())
L = [[0] * 10 for _ in range(10)]

for i in range(1,N+1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    L[a][b] += 1

ans = 0
for i in range(1,N+1):
    a = int(str(i)[0])
    b = int(str(i)[-1])
    ans += L[b][a]

print(ans)